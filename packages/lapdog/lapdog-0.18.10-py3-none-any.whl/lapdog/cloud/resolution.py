import os
try:
    from . import utils
except ImportError:
    import sys
    sys.path.append(os.path.dirname(__file__))
    import utils
import traceback
import sys
import json
from hashlib import sha512

@utils.cors("POST")
def insert_resolution(request):
    """
    This function is unique. It is not deployed into each project.
    It is deployed once into my personal project which serves as a centralized
    database.
    """
    logger = utils.CloudLogger().log_request(request)
    try:
        data = request.get_json()

        if not isinstance(data, dict):
            return (
                {
                    'error': "Bad Request",
                    'message': ("No data was provided" if data is None else "Expected JSON dictionary in request body")
                },
                400
            )

        token = utils.extract_token(request.headers, data)

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

        if 'namespace' not in data:
            return (
                {
                    'error': 'Missing Parameters',
                    'message': "Missing required parameter \"namespace\""
                },
                400
            )

        user_session = utils.generate_user_session(token)

        while True:
            response = user_session.get(
                'https://api.firecloud.org/api/profile/billing'
            )

            if response.status_code == 200:
                break
            print(response.status_code, response.text, file=sys.stderr)
            if response.status_code == 404:
                return (
                    {
                        'error': "User not found",
                        'message': "You are not registered yet with firecloud"
                    },
                    404
                )
            time.sleep(5)


        projects = {proj['projectName']:proj for proj in response.json()}
        if data['namespace'] not in projects:
            return (
                {
                    'error': "Bad Namespace",
                    'message': 'The provided namespace "%s" could not be found' % data['namespace']
                },
                400
            )

        if projects[data['namespace']]['role'] not in {'Owner', 'Admin', 'Administrator'}:
            return (
                {
                    'error': "Insufficient Permissions",
                    'message': "The user lacks Owner/Admin privilages on the provided namespace"
                },
                401
            )

        if 'project' not in data:
            return (
                {
                    'error': "Missing parameters",
                    'message': "Missing required parameter \"project\""
                },
                400
            )

        response = user_session.post(
            'https://cloudresourcemanager.googleapis.com/v1/projects/{project}:getIamPolicy'.format(
                project=data['project']
            )
        )

        if response.status_code == 403:
            return (
                {
                    'error': 'Unauthorized',
                    'message': "User lacks permissions on the provided project"
                },
                401
            )

        if response.status_code != 200:
            return (
                {
                    'error': 'Unexpected response from Googla API',
                    'message': '(%d) : %s' % (response.status_code, response.text)
                },
                400
            )

        for policy in response.json()['bindings']:
            if policy['role'] == 'roles/owner':
                if ('user:'+token_info['email']) in policy['members']:
                    blob = utils.getblob(
                        'gs://lapdog-resolutions/%s' % sha512(data['namespace'].encode()).hexdigest(),
                        credentials=utils.generate_default_session().credentials
                    )
                    if blob.exists():
                        return (
                            {
                                'error': "Already Exists",
                                'message': "A resolution for this namespace is already in place"
                            },
                            409
                        )
                    logger.log(
                        "Adding new resolution",
                        namespace=data['namespace'],
                        project_id=data['project'],
                        admin=token_info['email'],
                        severity='NOTICE'
                    )
                    blob.upload_from_string(
                        data['project'].encode()
                    )
                    return (
                        'gs://lapdog-resolutions/%s' % sha512(data['namespace'].encode()).hexdigest(),
                        200
                    )
        return (
            {
                'error': "Unauthorized",
                'message': "User lacks ownership of the provided project"
            },
            400
        )

    except:
        logger.log_exception()
        return (
            {
                'error': "Unknown Error",
                'message': traceback.format_exc()
            },
            500
        )
