from google.cloud import kms_v1 as kms, storage, logging
import google.auth
from google.cloud.logging.resource import Resource as LogResource
from google.auth.transport.requests import AuthorizedSession
import google.oauth2.service_account
import google.oauth2.credentials
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec, padding, utils
import requests
from hashlib import md5, sha256
import os
import json
from urllib.parse import quote
import time
from functools import lru_cache, wraps
import traceback

__API_VERSION__ = {
    'submit': 'v11',
    'abort': 'v3',
    'register': 'v6',
    'signature': 'v3',
    'query': 'v3',
    'quotas': 'v5',
    'resolve': 'v4',
    'oauth': 'v1',
    'update': 'v4',
    'existence': 'frozen'
}

# The api version will allow versioning of cloud functions
# The patching system will be as follows:
# End users who update their lapdog will encounter errors because the cloud endpoints do not exist
# End users contact administrators, asking them to update
# Administrators can run lapdog patch {namespace} (to be implemented)
# Lapdog patch will run code from lapdog.patch.__project_admin_apply_patch
# This function will deploy new cloud functions and run any other arbitrary code
# Such as updating iam policy bindings or role permissions

__CROMWELL_TAG__ = 'v0.17.0'

GCP_ZONES = {
    'asia-east1':	('a', 'b', 'c'),
    'asia-east2':	('a', 'b', 'c'),
    'asia-northeast1':	('a', 'b', 'c'),
    'asia-south1':	('a', 'b', 'c'),
    'asia-southeast1':	('a', 'b', 'c'),
    'australia-southeast1':	('a', 'b', 'c'),
    'europe-north1':	('a', 'b', 'c'),
    'europe-west1':	('b', 'c', 'd'),
    'europe-west2':	('a', 'b', 'c'),
    'europe-west3':	('a', 'b', 'c'),
    'europe-west4':	('a', 'b', 'c'),
    'northamerica-northeast1':	('a', 'b', 'c'),
    'southamerica-east1':	('a', 'b', 'c'),
    'us-central1':	('a', 'b', 'c', 'f'),
    'us-east1':	('b', 'c', 'd'),
    'us-east4':	('a', 'b', 'c'),
    'us-west1':	('a', 'b', 'c'),
    'us-west2':	('a', 'b', 'c'),
}

UPDATE_KEY_PATH = 'projects/broad-cga-aarong-gtex/locations/global/keyRings/lapdog/cryptoKeys/update-signing-key'
UPDATE_IMAGE_TAG = 'v1'

OAUTH_CLIENT_ID = '1057449931000-0mn07vdb6u3nhrvjkvr80qqbri0pvq7o.apps.googleusercontent.com'
AUTHENTICATION_URL = 'https://us-central1-broad-cga-aarong-gtex.cloudfunctions.net/oauth-{}'.format(__API_VERSION__['oauth'])

def cors(*methods):
    """
    Wraps functions intended to handle inbound flask requests. The wrapped
    function will have CORS policies applied as follows:
    1) OPTIONS requests are returned with the accepted list of methods and localhost only origins
    2) Issues 405 responses to requests with bad methods
    3) Issues 403 responses to requests with bad origins
    4) Passes on requests to the decorated function only if they have an accepted method and localhost origin
    """
    def wrapper(func):
        @wraps(func)
        def call(request):
            if request.method == 'OPTIONS':
                headers = {
                    'Access-Control-Allow-Origin': (
                        'http://localhost:4201' if not (
                            'Origin' in request.headers and request.headers['Origin'].startswith('http://localhost')
                        ) else request.headers['Origin']
                    ),
                    'Access-Control-Allow-Methods': ', '.join(methods),
                }
                return ('', 204, headers)
            elif request.method not in methods:
                return ('Not allowed', 405, {'Allow': ', '.join(methods)})
            elif 'Origin' in request.headers and not request.headers['Origin'].startswith('http://localhost'):
                return ('Forbidden', 403)
            response = requests.get("https://us-central1-a-graubert.cloudfunctions.net/ld-master-switch")
            if response.status_code != 200 or response.text != "OK":
                return (
                    (
                        "The Lapdog Master Switch has been disabled."
                        " Generally this means Lapdog has been taken offline"
                        " for security reasons. Check https://github.com/broadinstitute/lapdog"
                        " for updates"
                    ),
                    510
                )
            result = list(func(request))
            if isinstance(result[0], dict):
                result[0] = json.dumps(result[0])
            return tuple(result)
        return call
    return wrapper

## This is a redundant getblob
## However, google-cloud-functions seems to take issue with dalmatian

@lru_cache()
def _getblob_client(credentials):
    return storage.Client(credentials=credentials)

def getblob(gs_path, credentials=None, user_project=None):
    """
    Return a GCP "blob" object for a given gs:// path.
    Path must start with "gs://".
    By default, uses the current application default credentials for authentication.
    Alternatively, you may provide a `google.auth.Credentials` object.
    When interacting with a requester pays bucket, you must set `user_project` to
    be the name of the project to bill for the data transfer fees
    """
    if not gs_path.startswith('gs://'):
        raise ValueError("Getblob path must start with gs://")
    bucket_id = gs_path[5:].split('/')[0]
    bucket_path = '/'.join(gs_path[5:].split('/')[1:])
    return storage.Blob(
        bucket_path,
        _getblob_client(credentials).bucket(bucket_id, user_project)
    )


def extract_token(headers, data):
    if headers is not None and 'Authorization' in headers and headers['Authorization'].startswith("Bearer "):
        return headers['Authorization'][7:]
    elif data is not None and 'token' in data:
        return data['token']
    return None

def get_token_info(token_or_session):
    """
    Gets metadata for a given GCP access token or session
    """
    try:
        if isinstance(token_or_session, str):
            data = requests.get('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token='+token_or_session).json()
        else:
            data = token_or_session.get("https://www.googleapis.com/oauth2/v1/tokeninfo").json()
        return data
    except:
        return {
            "error": "Unknown Error",
            "error_description": traceback.format_exc()
        }

def validate_token(token_info):
    """
    Checks token authenticity
    """
    return (
        ('expires_in' in token_info and token_info['expires_in'] > 2)
        and ('email' in token_info and 'audience' in token_info)
        and (
            (not token_info['email'].endswith('@broadinstitute.org'))
            or token_info['audience'] == OAUTH_CLIENT_ID
        )
        and 'scope' in token_info
        and (
            'email' in token_info['scope']
            and 'profile' in token_info['scope']
            and 'openid' in token_info['scope']
            and 'https://www.googleapis.com/auth/devstorage.read_write' in token_info['scope']
        )
    )

def ld_acct_in_project(account, ld_project=None):
    """
    Gets a user's Pet account within a given lapdog engine project.
    Project must be specified unless function is executing within a cloud function
    """
    if ld_project is None:
        ld_project = os.environ.get('GCP_PROJECT')
    return ('lapdog-'+ md5(account.encode()).hexdigest())[:30] + '@' + ld_project + '.iam.gserviceaccount.com'

def ld_meta_bucket_for_project(ld_project=None):
    """
    Gets the metadata bucket id for a given lapdog engine project.
    Project must be specified unless function is executing within a cloud function
    """
    if ld_project is None:
        ld_project = os.environ.get('GCP_PROJECT')
    return 'ld-metadata-'+md5(ld_project.encode()).hexdigest()

def ld_project_for_namespace(namespace):
    """
    Gets the lapdog engine project for a given namespace
    """
    prefix = ('ld-'+namespace)[:23]
    suffix = md5(prefix.encode()).hexdigest().lower()
    return prefix + '-' + suffix[:6]

def proxy_group_for_user(account):
    """
    Gets a firecloud proxy group name for a given account
    """
    # ick!
    if account == 'jcha@broadinstitute.org':
        return 'jcha-lapdog'
    info = account.split('@')
    return info[0]+'-'+info[1].split('.')[0]+'-lapdog'

def generate_user_session(token):
    """
    Generates a Google AuthorizedSession from a provided access token
    """
    return AuthorizedSession(
        google.oauth2.credentials.Credentials(token)
    )

def generate_default_session(scopes=None):
    credentials, project = google.auth.default(scopes=scopes)
    session = AuthorizedSession(credentials)
    session._default_project = project
    return session

def generate_core_session():
    ld_project = os.environ.get('GCP_PROJECT')
    account = 'lapdog-worker@{}.iam.gserviceaccount.com'.format(ld_project)
    t = int(time.time())
    key_data = json.loads(getblob(
        'gs://{bucket}/auth_key.json'.format(
            bucket=ld_meta_bucket_for_project(ld_project)
        )
    ).download_as_string().decode())
    return AuthorizedSession(
        google.oauth2.service_account.Credentials.from_service_account_info(key_data).with_scopes([
            'https://www.googleapis.com/auth/cloud-platform',
            'https://www.googleapis.com/auth/genomics',
            'https://www.googleapis.com/auth/devstorage.read_write'
        ])
    )

def authenticate_bucket(bucket, namespace, workspace, session, core_session):
    """
    Used internally to authenticate a bucket for lapdog use
    """
    workspace_blob = getblob(
        'gs://{bucket}/DO_NOT_DELETE_LAPDOG_WORKSPACE_SIGNATURE'.format(
            bucket=bucket
        ),
        credentials=session.credentials
    )
    if not workspace_blob.exists():
        # Must generate signature
        resolution_blob = getblob(
            'gs://{bucket}/resolution'.format(
                bucket=ld_meta_bucket_for_project(os.environ.get('GCP_PROJECT'))
            )
        )
        if not resolution_blob.exists():
            return False, "No resolution found"
        if namespace != resolution_blob.download_as_string().decode():
            return False, 'This project is not responsible for the provided namespace'
        print("Generating new workspace signature for", workspace)
        try:
            response = session.get(
                'https://api.firecloud.org/api/workspaces/{namespace}/{workspace}'.format(
                    namespace=namespace,
                    workspace=workspace
                ),
                timeout=5 # Long timeout because this is a 1-time operation
            )
            if response.status_code == 200:
                fc_bucket = response.json()['workspace']['bucketName']
                if fc_bucket != bucket:
                    return False, 'The provided bucket does not belong to this workspace'
                sign_object(
                    ('{}/{}/{}'.format(namespace, workspace, bucket)).encode(),
                    workspace_blob,
                    core_session.credentials
                )
                return True, fc_bucket
        except requests.ReadTimeout:
            pass
        return False, 'The Firecloud API is currently offline or took too long to respond'
    return (
        verify_signature(workspace_blob, ('{}/{}/{}'.format(namespace, workspace, bucket)).encode()),
        'Workspace authentication token had an invalid signature'
    )

def get_crypto_keys(name, credentials):
    return sorted(
        (key.name for key in kms.KeyManagementServiceClient(credentials=credentials).list_crypto_key_versions(name) if key.state == 1),
        key=lambda name:int(name.split('/')[-1]),
        reverse=True
    )

def _get_signature(data, keypath, credentials):
    return kms.KeyManagementServiceClient(
        credentials=credentials
    ).asymmetric_sign(
        get_crypto_keys(keypath, credentials)[0],
        {'sha256': sha256(data).digest()}
    ).signature

def sign_object(data, blob, credentials, keypath=None):
    if keypath is None:
        keypath = 'projects/{ld_project}/locations/us/keyRings/lapdog/cryptoKeys/lapdog-sign'.format(ld_project=os.environ.get('GCP_PROJECT'))
    blob.upload_from_string(_get_signature(data, keypath, credentials))

def verify_signature(blob, data, keypath=None, credentials=None, _is_blob=True):
    if keypath is None:
        keypath = 'projects/{ld_project}/locations/us/keyRings/lapdog/cryptoKeys/lapdog-sign'.format(ld_project=os.environ.get('GCP_PROJECT'))
    if credentials is None:
        credentials = generate_default_session().credentials
    for key in get_crypto_keys(keypath, credentials):
        try:
            serialization.load_pem_public_key(
                kms.KeyManagementServiceClient().get_public_key(key).pem.encode('ascii'),
                default_backend()
            ).verify(
                blob.download_as_string() if _is_blob else blob,
                sha256(data).digest(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=32
                ),
                utils.Prehashed(hashes.SHA256())
            )
            return True
        except InvalidSignature:
            pass
    return False

def validate_permissions(session, bucket):
    try:
        response = session.get(
            "https://storage.googleapis.com/storage/v1/b/{bucket}"
            "/iam/testPermissions?permissions=storage.objects.list&"
            "permissions=storage.objects.get&permissions=storage.objects.create&"
            "permissions=storage.objects.delete".format(bucket=quote(bucket, safe='')),
        )
        if response.status_code == 200:
            data = response.json()
            if 'permissions' in data:
                canList = 'storage.objects.list' in data['permissions']
                canGet = 'storage.objects.get' in data['permissions']
                if canList and not canGet:
                    response = session.get(
                        "https://storage.googleapis.com/storage/v1/b/{}/o?maxResuls=50&fields=items/name".format(
                            bucket
                        )
                    )
                    if response.status_code == 200:
                        for item in response.json()['items']:
                            test = session.get(
                                'https://storage.googleapis.com/storage/v1/b/{}/o/{}'.format(
                                    bucket,
                                    quote(item['name'], safe='')
                                )
                            )
                            if test.status_code == 200:
                                canGet = True
                                break
                return (
                    canList and canGet,
                    'storage.objects.create' in data['permissions'] and 'storage.objects.delete' in data['permissions']
                )
            else:
                return False, False
        elif response.status_code == 401:
            data = response.json()
            if 'error' in data and 'message' in data['error']:
                if data['error']['message'] == 'Invalid Credentials':
                    return None, 'Expired Credentials'
                elif data['error']['message'] == 'Not Found':
                    return None, 'Bucket Not Found'
        return None, 'Invalid Credentials'
    except:
        return None, 'Unexpected Error'

def validate_submission_file(blob):
    if not blob.exists():
        return False, 'Submission.json file not found'
    blob.reload()
    if blob.size is None or blob.size >= 1073741824: # 1Gib
        return False, 'Submission.json file exceeded maximum allowed size'
    return True, 'OK'

def fetch_submission_blob(session, bucket, submission_id):
    return getblob(
        'gs://{bucket}/lapdog-executions/{submission_id}/submission.json'.format(
            bucket=bucket,
            submission_id=submission_id
        ),
        credentials=session.credentials
    )

def check_user_service_account(account, session=None):
    if session is None:
        session = generate_default_session([
            'https://www.googleapis.com/auth/cloud-platform',
            'https://www.googleapis.com/auth/iam'
        ])
    response = query_service_account(session, account)
    if response.status_code == 200:
        return response.json()
    return None

def query_service_account(session, account):
    return session.get(
        'https://iam.googleapis.com/v1/projects/{project}/serviceAccounts/{account}'.format(
            project=os.environ.get('GCP_PROJECT'),
            account=quote(account)
        )
    )

def update_iam_policy(session, grants, project=None):
    """
    Updates the IAM policy for a given project.
    `session` must be an AuthorizedSession for a user with sufficient permissions
    to update the project IAM policy.
    `grants` must be a dictionary of email:role, to grant in the project.
    Prepend each email with the account type ("user:john@example.net", "serviceAccount:accountName@project.iam.googleapis.com", "group:group@groups.google.com")
    `project` must be the lapdog engine project. Project is inferred automatically
    when running in a cloud function
    """
    if project is None:
        project = os.environ.get('GCP_PROJECT')
    policy = session.post(
        'https://cloudresourcemanager.googleapis.com/v1/projects/{project}:getIamPolicy'.format(
            project=project
        )
    ).json()
    for account_email, role in grants.items():
        target_role = 'projects/{}/roles/{}'.format(
            project,
            role
        )
        if target_role in {binding['role'] for binding in policy['bindings']}:
            for i, binding in enumerate(policy['bindings']):
                if binding['role'] == target_role:
                    policy['bindings'][i]['members'].append(
                        account_email
                    )
        else:
            policy['bindings'].append(
                {
                    'role': target_role,
                    'members': [
                        account_email
                    ]
                }
            )
    response = session.post(
        'https://cloudresourcemanager.googleapis.com/v1/projects/{project}:setIamPolicy'.format(
            project=project
        ),
        headers={'Content-Type': 'application/json'},
        json={
            "policy": policy,
            "updateMask": "bindings"
        }
    )
    return response.status_code == 200, response

def enabled_regions(project=None):
    blob = getblob('gs://{bucket}/regions'.format(bucket=ld_meta_bucket_for_project(project)))
    try:
        if blob.exists():
            return blob.download_as_string().decode().split()
    except:
        traceback.print_exc()
    return ['us-central1']

class CloudLogger(object):
    def __init__(self, function_name=None, function_region=None, function_project=None):
        self.logger = logging.Client(function_project).logger('lapdog-api-logging%2Fcloud-functions')
        self.resource = LogResource(
            type='cloud_function',
            labels={
                'function_name': os.environ.get("FUNCTION_NAME") if function_name is None else function_name,
                'project_id': os.environ.get("GCP_PROJECT") if function_project is None else function_project,
                'region': os.environ.get("FUNCTION_REGION") if function_region is None else function_region
            }
        )

    def log_request(self, request):
        headers = request.headers
        payload = request.get_json()
        self.log(
            json={
                'message': "Initialized logging with request ({})".format(
                    self.resource.labels['function_name']
                ),
                'request': {
                    'url': str(request.url),
                    'origin': headers['X-Forwarded-For'] if 'X-Forwarded-For' in headers else request.remote_addr,
                    'payload_size': request.content_length,
                    'content_type': request.content_type,
                    'headers': {
                        k:headers.getlist(k) if k not in {'Authorization', 'X-Fc-Auth'} else ['****************']
                        for k,v in headers
                    },
                    'payload': {
                        k:v if 'token' not in k else '****************'
                        for k,v in payload.items()
                    } if isinstance(payload, dict) else None
                }
            },
            severity='DEBUG'
        )
        return self

    def log_exception(self, message='Unhandled Exception'):
        self.log(
            message=message,
            traceback=traceback.format_exc(),
            severity='WARNING'
        )

    def log(self, text=None, json=None, severity='DEFAULT', **kwargs):
        if isinstance(severity, str):
            severity = {
                'DEFAULT': 0,
                'DEBUG': 100,
                'INFO': 200,
                'NOTICE': 300,
                'WARNING': 400,
                'WARN': 400,
                'ERROR': 500,
                'ERR': 500,
                'CRITICAL': 600,
                'ALERT': 700,
                'EMERGENCY': 800
            }[severity]
        if len(kwargs):
            if json is not None:
                json = {**json, **kwargs}
            else:
                json = kwargs
        # Mask user tokens
        if isinstance(json, dict) and 'token' in json:
            json['token'] = '****************'
        if text is None:
            if json is None:
                raise ValueError("No input provided")
            self.logger.log_struct(json, resource=self.resource, severity=severity)
        elif json is not None:
            self.logger.log_struct(
                {
                    'message': text,
                    'json': json
                },
                resource=self.resource,
                severity=severity
            )
        else:
            self.logger.log_text(
                text,
                resource=self.resource,
                severity=severity
            )
