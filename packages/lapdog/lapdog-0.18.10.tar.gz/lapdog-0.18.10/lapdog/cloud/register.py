import os
try:
    from . import utils
except ImportError:
    import sys
    sys.path.append(os.path.dirname(__file__))
    import utils
import google.auth
from google.auth.transport.requests import AuthorizedSession
import google.oauth2.service_account
import json
from urllib.parse import quote
import base64
import traceback
import requests
import time

@utils.cors("POST")
def register(request):
    logger = utils.CloudLogger().log_request(request)
    try:
        data = request.get_json()

        # 1) Validate the token

        if not isinstance(data, dict):
            return (
                {
                    'error': "Bad Request",
                    'message': ("No data was provided" if data is None else "Expected JSON dictionary in request body")
                },
                400
            )

        token = utils.extract_token(request.headers, data)
        if token is None:
            return (
                {
                    'error': 'Bad Request',
                    'message': 'Token must be provided in header or body'
                },
                400
            )

        token_info = utils.get_token_info(token)
        if 'error' in token_info:
            return (
                {
                    'error': 'Invalid Token',
                    'message': token_info['error_description'] if 'error_description' in token_info else 'Google rejected the client token'
                },
                401
            )

        if not utils.validate_token(token_info):
            return (
                {
                    'error': 'Rejected token',
                    'message': 'Token was valid but did not meet Lapdog security requirements. Token must have email, profile, openid, and devstorage.read_write scopes.'
                    ' Broad users must authenticate via a LapdogToken'
                },
                403
            )

        # 2) Validate user's permission for the bucket

        if 'bucket' not in data:
            return (
                {
                    'error': 'Bad Request',
                    'message': 'Missing required parameter "bucket"'
                },
                400
            )

        session = utils.generate_user_session(token)
        fc_auth = utils.generate_user_session(request.headers['X-Fc-Auth']) if 'X-Fc-Auth' in request.headers else None
        fc_auth_error = (
            'Authorized'
            if fc_auth is not None or 'cloud-platform' in token_info['scope'] else
            'Not Authorized. Repeat request with the "X-Fc-Auth" header containing application-default credentials'
        )

        if fc_auth is None:
            logger.log(
                "Missing backup Firecloud authentication",
                token_info=token_info,
                authorized=True if 'cloud-platform' in token_info['scope'] else False,
                severity='DEBUG'
            )

        read, write = utils.validate_permissions(session, data['bucket'])
        if read is None:
            # Error, write will contain a message
            return (
                {
                    'error': 'Cannot Validate Bucket Permissions',
                    'message': write
                },
                400
            )
        if not (read and write):
            # User doesn't have full permissions to the bucket
            return (
                {
                    'error': 'Not Authorized',
                    'message': 'User lacks read/write permissions to the requested bucket'
                },
                403
            )

        # 2.b) Verify that the bucket belongs to this project

        if 'namespace' not in data or 'workspace' not in data:
            return (
                {
                    'error': 'Bad Request',
                    'message': 'Missing required parameters "namespace" and "workspace"'
                },
                400
            )
        core_session = utils.generate_core_session()

        result, message = utils.authenticate_bucket(
            data['bucket'], data['namespace'], data['workspace'], fc_auth if fc_auth is not None else session, core_session
        )
        if not result:
            return (
                {
                    'error': 'Cannot Validate Bucket Signature',
                    'message': message,
                    'FC-Auth': fc_auth_error
                },
                400
            )

        # 3) Issue worker account

        default_session = utils.generate_default_session(scopes=['https://www.googleapis.com/auth/cloud-platform'])
        account_email = utils.ld_acct_in_project(token_info['email'])
        response = utils.query_service_account(default_session, account_email)
        if response.status_code == 404:
            account_name = account_email.split('@')[0]
            logger.log(
                'Issuing new pet service account',
                user=token_info['email'],
                service_account=account_email,
                severity='DEBUG'
            )
            response = default_session.post(
                'https://iam.googleapis.com/v1/projects/{project}/serviceAccounts'.format(
                    project=os.environ.get('GCP_PROJECT')
                ),
                headers={'Content-Type': 'application/json'},
                json={
                    'accountId': account_name,
                    'serviceAccount': {
                        'displayName': token_info['email']
                    }
                }
            )
            if response.status_code >= 400:
                return (
                    {
                        'error': 'Unable to issue service account',
                        'message': response.text
                    },
                    400
                )
        elif response.status_code >= 400:
            return (
                {
                    'error': 'Unable to query service account',
                    'message': response.text
                },
                400
            )
        if response.json()['email'] != account_email:
            return (
                {
                    'error': 'Service account email did not match expected value',
                    'message': response.json()['email'] + ' != ' + account_email
                },
                400
            )

        # 4) Update worker bindings

        logger.log(
            "Updating service account bindings",
            account=account_email,
            bindings={
                os.environ.get("FUNCTION_IDENTITY"): 'roles/iam.serviceAccountUser',
                account_email: 'roles/iam.serviceAccountUser'
            }
        )

        response = default_session.post(
            'https://iam.googleapis.com/v1/projects/{project}/serviceAccounts/{account}:setIamPolicy'.format(
                project=os.environ.get('GCP_PROJECT'),
                account=account_email
            ),
            headers={'Content-Type': 'application/json'},
            json={
                "policy": {
                    "bindings": [
                        {
                            "role": "roles/iam.serviceAccountUser",
                            "members": [
                                # Allows the gcloud functions account to set this pet account on comwell servers
                                "serviceAccount:{email}".format(email=os.environ.get("FUNCTION_IDENTITY")),
                                # Allows the service account to set itself as the compute account on cromwell workers
                                "serviceAccount:{email}".format(email=account_email)
                            ]
                        }
                    ]
                },
                "updateMask": "bindings"
            }
        )

        if response.status_code != 200:
            return (
                {
                    'error': 'Unable to update service account bindings',
                    'message': '(%d) : %s' % (response.status_code, response.text)
                }
            )

        # 5) Update project bindings

        logger.log(
            "Updating project-wide iam roles",
            bindings={
                account_email: 'Pet_account',
                token_info['email']: 'Lapdog_user'
            },
            severity="INFO"
        )

        status, response = utils.update_iam_policy(
            default_session,
            {
                'serviceAccount:'+account_email: 'Pet_account',
                'user:'+token_info['email']: 'Lapdog_user'
            }
        )

        if not status:
            return (
                {
                    'error': 'Unable to update project IAM policy',
                    'message': '(%d) : %s' % (response.status_code, response.text)
                },
                400
            )

        # 6) Generate Key

        logger.log(
            'Issuing new service account key',
            service_account=account_email
        )

        response = default_session.post(
            'https://iam.googleapis.com/v1/projects/{project}/serviceAccounts/{email}/keys'.format(
                project=os.environ.get('GCP_PROJECT'),
                email=quote(account_email)
            )
        )
        if response.status_code >= 400:
            return (
                {
                    'error': 'Unable to issue service account key',
                    'message': response.text
                },
                400
            )

        # 7) Register with Firecloud

        time.sleep(10) # New service account keys take a few seconds before they're usable

        # Register the user's new pet service account w/ Firecloud
        # We authenticate as the service account by using the newly generated key
        pet_session = AuthorizedSession(
            google.oauth2.service_account.Credentials.from_service_account_info(
                json.loads(base64.b64decode(response.json()['privateKeyData']).decode())
            ).with_scopes([
                'https://www.googleapis.com/auth/userinfo.profile',
                'https://www.googleapis.com/auth/userinfo.email'
            ])
        )
        while True:
            try:
                response = pet_session.post(
                    "https://api.firecloud.org/register/profile",
                    headers={
                        'User-Agent': 'FISS/0.16.9',
                        'Content-Type': 'application/json'
                    },
                    json={
                        "firstName":"Service",
                        "lastName": "Account",
                        "title":"None",
                        "contactEmail":token_info['email'],
                        "institute":"None",
                        "institutionalProgram": "None",
                        "programLocationCity": "None",
                        "programLocationState": "None",
                        "programLocationCountry": "None",
                        "pi": "None",
                        "nonProfitStatus": "false"
                    },
                    timeout=10
                )
                break
            except google.auth.exceptions.RefreshError:
                logger.log_exception("Service account key not ready")
                time.sleep(10) # need more time for key to propagate
        if response.status_code != 200:
            return (
                {
                    'error': "Unable to register account with firecloud",
                    'message': response.text
                },
                400
            )

        # 8) Check ProxyGroup
        # Either add the new service account to the user's lapdog@firecloud.org group
        # Or create the group, if it doesn't exist

        fc_session = fc_auth if fc_auth is not None else session

        response = fc_session.get('https://api.firecloud.org/api/groups', headers={'User-Agent': 'FISS/0.16.9'}, timeout=5)

        if response.status_code != 200:
            return (
                {
                    'error': "Unable to enumerate user's groups",
                    'message': response.text,
                    'FC-Auth': fc_auth_error
                },
                400
            )

        target_group = utils.proxy_group_for_user(token_info['email'])

        for group in response.json():
            if group['groupName'] == target_group:
                # 9) Register Account in Group
                response = fc_session.put(
                    'https://api.firecloud.org/api/groups/{group}/member/{email}'.format(
                        group=target_group,
                        email=quote(account_email)
                    ),
                    timeout=5
                )
                if response.status_code != 204:
                    return (
                        {
                            'error': 'Unable to add pet account to proxy group',
                            'message': "Please manually add {email} to {group}".format(
                                group=target_group,
                                email=quote(account_email)
                            ),
                            'FC-Auth': fc_auth_error
                        },
                        400
                    )
                else:
                    return (
                        account_email,
                        200
                    )

        # 8.b) Create Group
        response = session.post(
            'https://api.firecloud.org/api/groups/{group}'.format(
                group=target_group
            ),
            timeout=5
        )
        if response.status_code >= 400:
            return (
                {
                    'error': 'Unable to create Firecloud proxy group',
                    'message': response.text
                },
                400
            )
        # 9) Register Account in Group
        response = fc_session.put(
            'https://api.firecloud.org/api/groups/{group}/member/{email}'.format(
                group=target_group,
                email=quote(account_email)
            ),
            timeout=5
        )
        if response.status_code != 204:
            return (
                {
                    'error': 'Unable to add pet account to proxy group',
                    'message': "Please manually add {email} to {group}".format(
                        group=target_group+'@firecloud.org',
                        email=quote(account_email)
                    ),
                    'FC-Auth': fc_auth_error
                },
                400
            )
        else:
            return (
                account_email,
                200
            )
    except requests.ReadTimeout:
        logger.log_exception('Firecloud timeout')
        return (
            {
                'error': 'timeout to firecloud',
                'message': 'Took longer than 5 seconds for Firecloud to respond. Please try again later'
            },
            400
        )
    except:
        logger.log_exception()
        return (
            {
                'error': 'Unknown Error',
                'message': traceback.format_exc()
            },
            500
        )
