# Submission Gateway
# Use as a modular component for adapter to interact with submission
# If submission JSON does not contain version field or version is 1, gcloud compute instances ssh
# If submission JSON contains version and version is 2, ssh -i {lapdog ssh token} {instance ip}
# If SSH fails for any reason, save the exception and try reading the log
# If the log is not found, then you're SOL

from functools import lru_cache
from firecloud import api as fc
import requests
import subprocess
from hashlib import md5, sha512
from .cache import cached, cache_fetch, cache_write
import time
import warnings
import contextlib
import crayons
import os
import io
import json
from threading import RLock
from .cloud import RESOLUTION_URL
from .cloud.utils import get_token_info, ld_project_for_namespace, ld_meta_bucket_for_project, proxy_group_for_user, generate_default_session, update_iam_policy, enabled_regions, __API_VERSION__, GCP_ZONES
from .auth import get_gcloud_account, LapdogToken, BadDomain
from urllib.parse import quote
import google.api_core.exceptions
import sys
import tempfile
import base64
from agutil import cmd as run_cmd
from dalmatian import WorkspaceManager, getblob
import traceback
import re
from uuid import uuid4

CORE_PERMISSIONS = [
    "cloudkms.cryptoKeyVersions.useToSign",
    "cloudkms.cryptoKeyVersions.viewPublicKey",
    "cloudkms.cryptoKeyVersions.get",
    "cloudkms.cryptoKeyVersions.list",
    "resourcemanager.projects.get",
    "genomics.datasets.create",
    "genomics.datasets.delete",
    "genomics.datasets.get",
    "genomics.datasets.list",
    "genomics.datasets.update",
    "genomics.operations.cancel",
    "genomics.operations.create",
    "genomics.operations.get",
    "genomics.operations.list",
    "lifesciences.operations.cancel",
    "lifesciences.operations.get",
    "lifesciences.operations.list",
]

FUNCTIONS_PERMISSIONS = [
    "cloudkms.cryptoKeyVersions.viewPublicKey",
    "cloudkms.cryptoKeyVersions.get",
    "cloudkms.cryptoKeyVersions.list",
    "iam.serviceAccountKeys.create",
    "iam.serviceAccountKeys.delete",
    "iam.serviceAccountKeys.get",
    "iam.serviceAccountKeys.list",
    "iam.serviceAccounts.create",
    "iam.serviceAccounts.delete",
    "iam.serviceAccounts.get",
    "iam.serviceAccounts.getIamPolicy",
    "iam.serviceAccounts.list",
    "iam.serviceAccounts.setIamPolicy",
    "iam.serviceAccounts.update",
    "resourcemanager.projects.get",
    "genomics.operations.create",
    "genomics.operations.get",
    "genomics.operations.list",
    "resourcemanager.projects.getIamPolicy",
    "resourcemanager.projects.setIamPolicy",
    "compute.projects.get",
    "compute.regions.get",
    "compute.subnetworks.setPrivateIpGoogleAccess",
    "logging.logEntries.create",
    "lifesciences.operations.cancel",
    "lifesciences.operations.get",
    "lifesciences.operations.list",
    "lifesciences.workflows.run"
]

ADMIN_PERMISSIONS = [
    "cloudfunctions.functions.call",
    "cloudfunctions.functions.create",
    "cloudfunctions.functions.get",
    "cloudfunctions.functions.list",
    "cloudfunctions.functions.sourceCodeGet",
    "cloudfunctions.functions.sourceCodeSet",
    "cloudfunctions.functions.update",
    "cloudfunctions.operations.get",
    "cloudfunctions.operations.list",
    "cloudfunctions.functions.getIamPolicy",
    "cloudfunctions.functions.setIamPolicy",
    "compute.networks.get",
    "compute.networks.list",
    "compute.networks.use",
    "compute.subnetworks.get",
    "compute.subnetworks.list",
    "compute.subnetworks.setPrivateIpGoogleAccess",
    "compute.subnetworks.update",
    "iam.roles.create",
    "iam.roles.get",
    "iam.roles.list",
    "iam.roles.update",
    "iam.serviceAccounts.get",
    "iam.serviceAccounts.list",
    "iam.serviceAccounts.create",
    'iam.serviceAccounts.setIamPolicy',
    'iam.serviceAccounts.getIamPolicy',
    "resourcemanager.projects.setIamPolicy",
    "resourcemanager.projects.getIamPolicy",
    "storage.objects.setIamPolicy",
    "storage.objects.update",
    "storage.buckets.get",
    "storage.objects.create",
    "storage.objects.delete",
    "storage.objects.get",
    "storage.objects.getIamPolicy",
    "storage.objects.list",
    "serviceusage.quotas.get",
    "serviceusage.quotas.update",
    "serviceusage.services.enable",
    "serviceusage.services.get",
    "serviceusage.services.list"
]

PET_PERMISSIONS = [
    "cloudkms.cryptoKeyVersions.viewPublicKey",
    "resourcemanager.projects.get",
    "genomics.operations.cancel",
    "genomics.operations.create",
    "genomics.operations.get",
    "genomics.operations.list",
    "serviceusage.services.use", # for requester pays
    "logging.logEntries.create",
    "lifesciences.operations.cancel",
    "lifesciences.operations.get",
    "lifesciences.operations.list",
    "lifesciences.workflows.run"
]

USER_PERMISSIONS = [
    "genomics.operations.get",
    "lifesciences.operations.get",
]

LAPDOG_SERVICES = [
    'cloudapis.googleapis.com',
    'clouddebugger.googleapis.com',
    'cloudfunctions.googleapis.com',
    'cloudkms.googleapis.com',
    'cloudresourcemanager.googleapis.com',
    'cloudtrace.googleapis.com',
    'compute.googleapis.com',
    'deploymentmanager.googleapis.com',
    'genomics.googleapis.com',
    'iam.googleapis.com',
    'iamcredentials.googleapis.com',
    'lifesciences.googleapis.com',
    'logging.googleapis.com',
    'servicemanagement.googleapis.com',
    'storage-component.googleapis.com',
    'storage-api.googleapis.com'
]

_ACL_LOCK = RLock()

creation_success_pattern = re.compile(r'Workspace (.+)/(.+) successfully')

id_rsa = os.path.join(
    os.path.expanduser('~'),
    '.ssh',
    'id_rsa'
)

credentials_file = os.path.join(
    os.path.expanduser('~'),
    '.config',
    'gcloud',
    'application_default_credentials.json'
)

def get_proxy_account(user_acct=None):
    if user_acct is None:
        user_acct = get_application_default_account()
    email = cache_fetch('proxy-acct', user_acct)
    if email is not None:
        return email
    acct = proxy_group_for_user(user_acct)
    response = fc.__get('/api/groups/{}'.format(acct))
    if response.status_code == 200:
        email = response.json()['groupEmail']
        if email == acct + '@firecloud.org':
            cache_write(email, 'proxy-acct', user_acct)
            return email

@lru_cache()
def get_application_default_account():
    """
    Gets the currently logged in gcloud application-default account.
    This checks application default credentials used by lapdog (gcloud auth application-default login)
    Not main credentials (gcloud auth login)
    LRU-cache because response cannot change after session is generated
    """
    return get_token_info(generate_default_session())['email']

_GLOBAL_LD_TOKEN_INTERNAL = None
_GLOBAL_LD_LOCK_INTERNAL = RLock()

def get_user_session():
    """
    Gets an authorized session usable for the Lapdog API.
    Currently not sufficent for register and submit endpoints, which may require
    additional credentials to authenticate buckets.
    """
    global _GLOBAL_LD_TOKEN_INTERNAL
    with _GLOBAL_LD_LOCK_INTERNAL:
        if _GLOBAL_LD_TOKEN_INTERNAL is None:
            try:
                _GLOBAL_LD_TOKEN_INTERNAL = LapdogToken()
            except BadDomain:
                print("LapdogToken system does not support non-Broad emails")
                print("Switching to legacy OAuth system")
                _GLOBAL_LD_TOKEN_INTERNAL = lambda x:None # dummy object
                _GLOBAL_LD_LOCK_INTERNAL.authorized_session = generate_default_session(scopes=[
                'profile',
                'email',
                'openid',
                'https://www.googleapis.com/auth/devstorage.read_write',
            ])
            try:
                from hound.client import _getblob_bucket
                for blob in _getblob_bucket(None, 'lapdog-alerts', None).list_blobs():
                    content = json.loads(blob.download_as_string().decode())
                    if content['type'] == 'critical':
                        text = content['text'] if 'text' in content else content['content']
                        print(crayons.red("Critical Alert:"), text)
            except:
                traceback.print_exc()
                warnings.warn("Unable to check Lapdog global alerts during startup")
        return _GLOBAL_LD_TOKEN_INTERNAL.authorized_session

@contextlib.contextmanager
def capture(display=True):
    """
    Context manager to redirect stdout and err
    """
    try:
        stdout_buff = io.StringIO()
        stderr_buff = io.StringIO()
        with contextlib.redirect_stdout(stdout_buff):
            with contextlib.redirect_stderr(stderr_buff):
                yield (stdout_buff, stderr_buff)
    finally:
        stdout_buff.seek(0,0)
        stderr_buff.seek(0,0)
        if display:
            print(stderr_buff.read(), end='', file=sys.stderr)
            stderr_buff.seek(0,0)
            print(stdout_buff.read(), end='')
            stdout_buff.seek(0,0)

def _generate_core_key_internal(ld_project, worker_account, session=None):
    """
    Issues a new core service account access key for a given lapdog engine project.
    This cannot be used unless you are an administrator.
    There is no reason to use this function unless:
    1) The current access key has expired (~10yr after generation)
    2) Someone has gained unauthorized access to the current key

    In the second case, you should log into the cloud console and remove any current
    keys for the core service account before calling this function. You should also
    check the acl bindings to ensure that no unathorized users have access to the metadata bucket
    either directly on object in the bucket or inheriting through project-level permissions
    You should also add a new key version of the lapdog-sign key in google KMS and
    remove all existing versions
    """
    if session is None:
        session = get_user_session()
    warnings.warn("Generating new root authentication key for project")
    response = session.post(
        "https://iam.googleapis.com/v1/projects/{project}/serviceAccounts/{account}/keys".format(
            project=quote(ld_project, safe=''),
            account=quote('lapdog-worker@{}.iam.gserviceaccount.com'.format(ld_project), safe='')
        )
    )
    if response.status_code == 200:
        blob = getblob(
            'gs://{bucket}/auth_key.json'.format(
                bucket=ld_meta_bucket_for_project(ld_project)
            )
        )
        blob.upload_from_string(
            base64.b64decode(response.json()['privateKeyData'].encode())
        )
        acl = blob.acl
        for entity in acl.get_entities():
            if entity.type == 'project':
                if entity.identifier.startswith('editors-'):
                    entity.revoke_owner()
                elif entity.identifier.startswith('viewers-'):
                    entity.revoke_read()
        acl.user(worker_account).grant_read()
        acl.save()
    else:
        print("(%d) : %s" % (response.status_code, response.text), file=sys.stderr)
        raise ValueError("Could not generate core key")

def resolve_project_for_namespace(namespace):
    resolution = cache_fetch('namespace', 'resolution', namespace=namespace)
    if resolution is None:
        blob = getblob(
            'gs://lapdog-resolutions/' + sha512(namespace.encode()).hexdigest()
        )
        if not blob.exists():
            raise NameError("No resolution for "+namespace)
        resolution = blob.download_as_string().decode()
        try:
            # Before caching the resolution, check the inverse
            # The resolved project should report that it manages the provided namespace
            # It would be unusual if it did not, perhaps a resolution was manually changed
            local_blob = getblob(
                'gs://{}/resolution'.format(ld_meta_bucket_for_project(resolution))
            )
            if local_blob.exists() and local_blob.download_as_string().decode() == namespace:
                cache_write(resolution, 'namespace', 'resolution', namespace=namespace)
        except:
            traceback.print_exc()
    return resolution

class Gateway(object):
    """
    Acts as an interface between local lapdog and any resources behind the project's API
    """
    def __init__(self, namespace):
        self.namespace = namespace
        try:
            self.project = resolve_project_for_namespace(namespace)
        except:
            self.project = None
            traceback.print_exc()
        try:
            if not self.exists:
                warnings.warn("Gateway does not exist. You will not be able to execute jobs")
            elif not self.registered:
                warnings.warn(
                    "Gateway for namespace {} not registered. Please run Gateway.register()".format(
                        self.namespace
                    )
                )
        except ValueError:
            traceback.print_exc()
            print("Gateway not up to date", file=sys.stderr)

    @classmethod
    def initialize_lapdog_for_project(cls, billing_id, project_id, custom_lapdog_project=None):
        """
        Initializes the lapdog execution API on the given firecloud project.
        Charges for operating the Lapdog API and for executing jobs will be billed
        to the provided billing id.
        The current gcloud account (when this function is executed) will be the Owner
        of the service and the only user capable of using it.
        Specify custom_lapdog_project to override default namespace->project association
        """
        if custom_lapdog_project is None:
            custom_lapdog_project = ld_project_for_namespace(project_id)
        print("Checking prerequisites")
        cmd = (
            'gcloud --version'
        )
        print(cmd)
        result = run_cmd(cmd)
        gcloud_version = {}
        for line in result.buffer.decode().split('\n'):
            if len(line.strip()):
                words = line.strip().split()
                gcloud_version[' '.join(words[:-1])] = int(words[-1].split('.')[0])
        if gcloud_version['Google Cloud SDK'] < 241:
            print("Update gcloud SDK? Lapdog requires >= 241.0.0")
            choice = input("Y/N : ")
            if not choice.strip().lower().startswith('y'):
                raise ValueError("Lapdog requires gcloud version >= 241.0.0; Please run 'gcloud components update'")
            print('gcloud components update')
            run_cmd('gcloud components update')
        if not ('alpha' in gcloud_version and 'beta' in gcloud_version):
            print("Install additional components? Lapdog requires gcloud alpha and beta")
            choice = input("Y/N : ")
            if not choice.strip().lower().startswith('y'):
                raise ValueError("Lapdog requires gcloud alpha and beta; Please run 'gcloud components install alpha beta'")
            print('gcloud components install alpha beta')
            run_cmd('gcloud components install alpha beta')

        print("Testing permissions")
        test_url = "https://cloudbilling.googleapis.com/v1/billingAccounts/{billing_account}:testIamPermissions".format(
            billing_account=billing_id
        )
        print("POST", test_url)
        user_session = generate_default_session()
        response = user_session.post(
            test_url,
            headers={"Content-Type": "application/json"},
            json={
                "permissions": [
                    "billing.accounts.get",
                    "billing.accounts.getIamPolicy",
                    "billing.resourceAssociations.create"
                ]
            }
        )
        if response.status_code != 200:
            raise ValueError("Unexpected response from Google API: ({}): {}".format(response.status_code, response.text))
        permissions = response.json()
        if 'permissions' not in permissions:
            raise ValueError("Unexpected response from Google API: %s. You may not have appropriate permissions for the billing account" % response.text)
        permissions = permissions['permissions']
        if "billing.accounts.get" not in permissions or "billing.accounts.getIamPolicy" not in permissions or "billing.resourceAssociations.create" not in permissions:
            raise ValueError("Insufficient permissions to use this billing account")

        print("GET https://api.firecloud.org/api/profile/billing")
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
        if project_id not in projects:
            raise NameError("The provided namespace '%s' could not be found" % project_id)

        if projects[project_id]['role'] not in {'Owner', 'Admin', 'Administrator'}:
            raise ValueError("You lack Owner/Admin privilages on the provided namespace")

        cmd = (
            'gcloud projects create {project_id}'.format(
                project_id=custom_lapdog_project
            )
        )
        print("Creating project")
        print(cmd)
        result = run_cmd(cmd)
        if result.returncode != 0:
            if b'already in use' not in result.buffer:
                raise ValueError("Unable to create project")
            else:
                print("This project is already in use")
                print("Do you wish to continue initialization with the given project?")
                choice = input("Y/N : ")
                if not choice.strip().lower().startswith('y'):
                    print("Aborted")
                    return
        cmd = 'gcloud --project {project} services enable cloudbilling.googleapis.com'.format(
            project=custom_lapdog_project,
        )
        print(cmd)
        subprocess.check_call(cmd, shell=True)
        cmd = 'gcloud --project {project} services enable serviceusage.googleapis.com'.format(
            project=custom_lapdog_project,
        )
        print(cmd)
        subprocess.check_call(cmd, shell=True)
        cmd = (
            'gcloud beta billing projects link {project_id} --billing-account '
            '{billing_id}'.format(
                project_id=custom_lapdog_project,
                billing_id=billing_id
            )
        )
        print("Enabling billing")
        print(cmd)
        subprocess.check_call(cmd, shell=True)
        print("Saving Namespace Resolution")
        response = user_session.post(
            RESOLUTION_URL,
            headers={"Content-Type": "application/json"},
            json={
                'namespace': project_id,
                'project': custom_lapdog_project
            }
        )
        if response.status_code == 409:
            proj = resolve_project_for_namespace(project_id)
            if proj != custom_lapdog_project:
                raise NameError("A resolution is already in place for this namespace. Please contact GitHub @agraubert")
        elif response.status_code != 200:
            print("(%d) : %s" % (response.status_code, response.text), file=sys.stderr)
            raise ValueError("Error when generating resolution")
        print("Enabling servies...")
        for service in LAPDOG_SERVICES:
            cmd = 'gcloud --project {project} services enable {service}'.format(
                project=custom_lapdog_project,
                service=service
            )
            print(cmd)
            subprocess.check_call(cmd, shell=True)
        print("Creating Signing Key")
        cmd = (
            'gcloud --project {project} kms keyrings create lapdog --location us'.format(
                project=custom_lapdog_project
            )
        )
        print(cmd)
        result = run_cmd(cmd)
        if result.returncode != 0 and b'ALREADY_EXISTS' not in result.buffer:
            raise ValueError("Unable to create Keyring")
        cmd = (
            'gcloud --project {project} alpha kms keys create lapdog-sign --location us --keyring'
            ' lapdog --purpose asymmetric-signing --default-algorithm '
            'rsa-sign-pss-3072-sha256 --protection-level software'.format(
                project=custom_lapdog_project
            )
        )
        print(cmd)
        result = run_cmd(cmd)
        if result.returncode != 0 and b'ALREADY_EXISTS' not in result.buffer:
            raise ValueError("Unable to create signing key")

        print("Creating Lapdog Roles")
        roles_url = "https://iam.googleapis.com/v1/projects/{project}/roles".format(
            project=custom_lapdog_project
        )
        print("POST", roles_url)
        response = user_session.post(
            roles_url,
            headers={
                'Content-Type': 'application/json'
            },
            json={
                "roleId": "Pet_account",
                "role": {
                    "title": "Pet_account",
                    "includedPermissions": PET_PERMISSIONS,
                    "stage": "GA"
                }
            }
        )
        if response.status_code != 200 and 'ALREADY_EXISTS' not in response.text:
            print("(%d) : %s" % (response.status_code, response.text), file=sys.stderr)
            raise ValueError("Invalid response from Google API")
        print("POST", roles_url)
        response = user_session.post(
            roles_url,
            headers={
                'Content-Type': 'application/json'
            },
            json={
                "roleId": "Core_account",
                "role": {
                    "title": "Core_account",
                    "includedPermissions": CORE_PERMISSIONS,
                    "stage": "GA"
                }
            }
        )
        if response.status_code != 200 and 'ALREADY_EXISTS' not in response.text:
            print("(%d) : %s" % (response.status_code, response.text), file=sys.stderr)
            raise ValueError("Invalid response from Google API")
        print("POST", roles_url)
        response = user_session.post(
            roles_url,
            headers={
                'Content-Type': 'application/json'
            },
            json={
                "roleId": "Functions_account",
                "role": {
                    "title": "Functions_account",
                    "includedPermissions": FUNCTIONS_PERMISSIONS,
                    "stage": "GA"
                }
            }
        )
        if response.status_code != 200 and 'ALREADY_EXISTS' not in response.text:
            print("(%d) : %s" % (response.status_code, response.text), file=sys.stderr)
            raise ValueError("Invalid response from Google API")
        print("POST", roles_url)
        response = user_session.post(
            roles_url,
            headers={
                'Content-Type': 'application/json'
            },
            json={
                "roleId": "Engine_Admin",
                "role": {
                    "title": "Engine_Admin",
                    "includedPermissions": ADMIN_PERMISSIONS,
                    "stage": "GA"
                }
            }
        )
        if response.status_code != 200 and 'ALREADY_EXISTS' not in response.text:
            print("(%d) : %s" % (response.status_code, response.text), file=sys.stderr)
            raise ValueError("Invalid response from Google API")
        print("POST", roles_url)
        response = user_session.post(
            roles_url,
            headers={
                'Content-Type': 'application/json'
            },
            json={
                "roleId": "Lapdog_user",
                "role": {
                    "title": "Lapdog_user",
                    "includedPermissions": USER_PERMISSIONS,
                    "stage": "GA"
                }
            }
        )
        if response.status_code != 200 and 'ALREADY_EXISTS' not in response.text:
            print("(%d) : %s" % (response.status_code, response.text), file=sys.stderr)
            raise ValueError("Invalid response from Google API")

        print("Creating Core Service Account")
        cmd = (
            'gcloud --project {project} iam service-accounts create lapdog-worker --display-name lapdog-worker'.format(
                project=custom_lapdog_project
            )
        )
        print(cmd)
        result = run_cmd(cmd)
        if result.returncode != 0 and b'already exists' not in result.buffer:
            raise ValueError("Unable to create service account")
        core_account = 'lapdog-worker@{}.iam.gserviceaccount.com'.format(custom_lapdog_project)
        print("Creating Cloud Functions Service Account")
        cmd = (
            'gcloud --project {project} iam service-accounts create lapdog-functions --display-name lapdog-functions'.format(
                project=custom_lapdog_project
            )
        )
        print(cmd)
        result = run_cmd(cmd)
        if result.returncode != 0 and b'already exists' not in result.buffer:
            raise ValueError("Unable to create service account")
        functions_account = 'lapdog-functions@{}.iam.gserviceaccount.com'.format(custom_lapdog_project)
        print("Creating Self-Updater Service Account")
        cmd = (
            'gcloud --project {project} iam service-accounts create lapdog-update --display-name lapdog-update'.format(
                project=custom_lapdog_project
            )
        )
        print(cmd)
        result = run_cmd(cmd)
        if result.returncode != 0 and b'already exists' not in result.buffer:
            raise ValueError("Unable to create service account")
        update_account = 'lapdog-update@{}.iam.gserviceaccount.com'.format(custom_lapdog_project)
        iam_url = 'https://iam.googleapis.com/v1/projects/{project}/serviceAccounts/{account}:setIamPolicy'.format(
            project=custom_lapdog_project,
            account=update_account
        )
        print("POST", iam_url)
        response = user_session.post(
            iam_url,
            headers={'Content-Type': 'application/json'},
            json={
                "policy": {
                    "bindings": [
                        {
                            "role": "roles/iam.serviceAccountUser",
                            "members": [
                                # Allows the gcloud functions account to set this pet account on comwell servers
                                "serviceAccount:{email}".format(email=functions_account),
                            ]
                        }
                    ]
                },
                "updateMask": "bindings"
            }
        )
        if response.status_code != 200:
            raise ValueError("Unexpected response from Google (%d) : %s" % (response.status_code, response.text))
        print("Creating Metadata bucket while service accounts are created")
        cmd = (
            'gsutil mb -c Standard -l us-central1 -p {project} gs://{bucket}'.format(
                project=custom_lapdog_project,
                bucket=ld_meta_bucket_for_project(custom_lapdog_project)
            )
        )
        print(cmd)
        result = run_cmd(cmd)
        if result.returncode != 0 and b'already exists' not in result.buffer:
            raise ValueError("Unable to create bucket")
        print("Updating project IAM policy while service accounts are created")
        policy = {
            'serviceAccount:'+core_account: 'Core_account',
            'serviceAccount:'+functions_account: 'Functions_account',
            'serviceAccount:'+update_account: 'Engine_Admin'
        }
        print(policy)
        status, response = update_iam_policy(
            user_session,
            policy,
            custom_lapdog_project
        )
        if not status:
            print('(%d) : %s' % (response.status_code, response.text), file=sys.stderr)
            raise ValueError("Invalid Response from Google API")
        print("Waiting for service account creation...")
        time.sleep(30)
        print("Issuing Core Service Account Key")
        _generate_core_key_internal(custom_lapdog_project, functions_account, user_session)
        print("Saving Project Resolution to Engine")
        blob = getblob(
            'gs://{bucket}/resolution'.format(
                bucket=ld_meta_bucket_for_project(custom_lapdog_project)
            )
        )
        blob.upload_from_string(project_id.encode())
        acl = blob.acl
        acl.all_authenticated().grant_read()
        acl.save()
        print("Configuring VPC Subnet")
        subnet_url = "https://www.googleapis.com/compute/v1/projects/{project}/regions/us-central1/subnetworks/default/setPrivateIpGoogleAccess".format(
            project=custom_lapdog_project
        )
        print("POST", subnet_url)
        response = user_session.post(
            subnet_url,
            headers={
                'Content-Type': "application/json"
            },
            params={
                'requestId': str(uuid4())
            },
            json={
                "privateIpGoogleAccess": True
            }
        )
        if response.status_code >= 400:
            raise ValueError("Unexpected response from Google (%d) : %s" % (response.status_code, response.text))
        print("Deploying Cloud Functions")
        from .cloud import _deploy
        _deploy('update', 'update', functions_account, custom_lapdog_project)
        _deploy('create_submission', 'submit', functions_account, custom_lapdog_project)
        _deploy('abort_submission', 'abort', functions_account, custom_lapdog_project)
        _deploy('check_abort', 'signature', functions_account, custom_lapdog_project)
        _deploy('register', 'register', functions_account, custom_lapdog_project)
        _deploy('query_account', 'query', functions_account, custom_lapdog_project)
        _deploy('quotas', 'quotas', functions_account, custom_lapdog_project)
        # Important that existence is deployed last
        # Once deployed, lapdog gateways will start reporting that the Engine is active
        _deploy('existence', 'existence', functions_account, custom_lapdog_project)

    @property
    def registered(self):
        """
        Property. Verifies that the current user is registered with this gateway
        """
        response = get_user_session().post(
            self.get_endpoint('query'),
        )
        return response.status_code == 200

    def register(self, workspace, bucket):
        """
        Registers the currently logged in account with the api
        Must provide a workspace name and the associated bucket to prove that you have access
        to at least one workspace for this namespace
        """
        # FIXME: Identify better authorization scheme for firecloud
        session = generate_default_session()
        get_token_info(session)
        warnings.warn("[BETA] Gateway Register")
        response = get_user_session().post(
            self.get_endpoint('register'),
            headers={
                'Content-Type': 'application/json',
                'X-Fc-Auth': session.credentials.token
            },
            json={
                'bucket': bucket,
                'namespace': self.namespace,
                'workspace': workspace,
            }
        )
        if response.status_code != 200:
            print("(%d) : %s" % (response.status_code, response.text), file=sys.stderr)
            raise ValueError("Gateway failed to register user")
        return response.text # your account email

    def create_submission(self, workspace, bucket, submission_id, workflow_options=None, use_cache=True, memory=3, private=False, region=None, _cache_size=None):
        """
        Sends a request through the lapdog execution API to start a new submission.
        Takes the local submission ID.
        Assumes the following files to be in place:
        Workflow Inputs : gs://{workspace bucket}/lapdog-executions/{submission id}/config.json
        Workflow WDL : gs://{workspace bucket}/lapdog-executions/{submission id}/method.wdl
        Submission JSON: gs://{workspace bucket}/lapdog-executions/{submission id}/submission.json

        The user will already have needed access to the workspace in order to evaluate
        workflow inputs.
        The user must have been granted access to the lapdog execution API for this
        workspace's namespace in order for the API to accept the request.
        The user's service account must have access to the workspace in order to
        download the input files specified in the workflow inputs.
        """
        # FIXME: Identify better authorization scheme for firecloud
        session = generate_default_session()
        get_token_info(session)
        warnings.warn("[BETA] Gateway Create Submission")
        if _cache_size is None and use_cache:
            blob = getblob('gs://{}/lapdog-call-cache.sql'.format(bucket))
            if blob.exists():
                blob.reload()
                _cache_size = blob.size
        response = get_user_session().post(
            self.get_endpoint('submit'),
            headers={
                'Content-Type': 'application/json',
                'X-Fc-Auth': session.credentials.token,
            },
            json={
                'bucket': bucket,
                'submission_id': submission_id,
                'namespace': self.namespace,
                'workspace': workspace,
                'workflow_options': workflow_options if workflow_options is not None else {},
                'memory': memory*1024,
                'no_ip': private,
                'compute_region': region,
                'callcache': use_cache,
                'cache_size': _cache_size / 1073741824 # 1gib
            }
        )
        if response.status_code == 200:
            operation = response.text
            submission_data_path = 'gs://{bucket}/lapdog-executions/{submission_id}/submission.json'.format(
                bucket=bucket,
                submission_id=submission_id
            )
            blob = getblob(submission_data_path)

            blob.upload_from_string(
                json.dumps(
                    {
                        **json.loads(blob.download_as_string().decode()),
                        **{'operation': operation}
                    }
                ).encode()
            )
            cache_write(
                "{}/{}/{}".format(
                    self.namespace,
                    workspace,
                    submission_id
                ),
                'submission-pointer',
                bucket,
                submission_id
            )
            return True, operation
        return False, response


    def abort_submission(self, bucket, submission_id, hard=False):
        """
        Sends a request through the lapdog execution API to abort a running submission.
        Takes the local submission ID and a list of operations corresponding to
        the workflow calls
        Assumes the following file to be in place:
        Submission JSON: gs://{workspace bucket}/lapdog-executions/{submission id}/submission.json

        Cancels the cromwell server operation then cancels all workflow operations,
        then deletes all workflow machines, then finally the cromwell machine.
        """
        warnings.warn("[BETA] Gateway Abort Submission")
        response = get_user_session().delete(
            self.get_endpoint('abort'),
            headers={'Content-Type': 'application/json'},
            json={
                'bucket': bucket,
                'submission_id': submission_id,
                'hard': hard
            }
        )
        if response.status_code != 200:
            return response

    def get_endpoint(self, endpoint, _version=None):
        """
        1) Generates the appropriate url for a given endpoint in this project
        2) Checks that the endpoint exists by submitting an OPTIONS request
        3) Returns the full endpoint url
        """
        if self.project is None:
            raise ValueError("No resolution for namespace %s. Project may not be initialized. Please contact the namespace admin" % self.namespace)
        if _version is None:
            if endpoint not in __API_VERSION__:
                raise KeyError("Endpoint not defined: "+endpoint)
            _version = __API_VERSION__[endpoint]
        endpoint_url = 'https://us-central1-{project}.cloudfunctions.net/{endpoint}-{version}'.format(
            project=self.project,
            endpoint=quote(endpoint),
            version=_version
        )
        response = get_user_session().options(endpoint_url)
        if response.status_code == 204:
            return endpoint_url
        if response.status_code == 200 or response.status_code == 404:
            print("Lapdog Engine Project", self.project, "for namespace", self.namespace, "does not support api version", _version, file=sys.stderr)
            if endpoint =='existence':
                raise ValueError("The existence endpoint could not be found. Project %s may not be initialized. Please contact the namespace admin" % self.project)
            raise ValueError("The project api for %s does not support %s version %s. Please contact the namespace admin" % (
                self.project,
                endpoint,
                _version
            ))
        raise ValueError("Unexpected status (%d) when checking for endpoint:" % response.status_code, response.text)

    @property
    def exists(self):
        """
        Property. Checks that the current Gateway actually exists.
        Checks that a specific internal endpoint exists and returns the expected response
        """
        try:
            response = get_user_session().get(self.get_endpoint('existence'))
            return response.status_code == 200 and response.text == 'OK'
        except ValueError:
            return False

    @property
    def quota_usage(self):
        """
        Property. Connects to the Gateway to fetch the current quota usage
        """
        warnings.warn("[BETA] Gateway Quotas")
        response = get_user_session().post(
            self.get_endpoint('quotas'),
        )
        if response.status_code == 200:
            return response.json()
        print("Quota error (%d) : %s" % (response.status_code, response.text), file=sys.stderr)
        raise ValueError("Unable to fetch quotas: status %d" % response.status_code)

    @property
    def compute_regions(self):
        if self.project is None:
            raise ValueError("Unable to check compute regions without a working Engine")
        return enabled_regions(self.project)

    @compute_regions.setter
    def compute_regions(self, regions):
        """
        Sets the list of allowed compute regions for this gateway.
        You must have Editor permissions to the project for this namespace
        """
        if self.project is None:
            raise ValueError("Unable to set compute regions without a working Engine")
        if len(regions) <= 0:
            raise ValueError("Must provide at least one compute region")
        user_session = get_user_session()
        print("Checking VPC configuration for new regions")
        for region in regions:
            if region not in GCP_ZONES:
                raise NameError(region + " is not a valid GCP Region")
            subnet_url = "https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/subnetworks/default".format(
                project=self.project,
                region=region
            )
            response = user_session.get(subnet_url)
            if response.status_code != 200:
                raise ValueError("Unexpected response from Google (%d) : %s" % (response.status_code, response.text))
            subnet = response.json()
            if not ('privateIpGoogleAccess' in subnet and subnet['privateIpGoogleAccess']):
                print("Updating VPC Subnet configuration for", region)
                response = user_session.post(
                    subnet_url+'/setPrivateIpGoogleAccess',
                    headers={
                        'Content-Type': "application/json"
                    },
                    params={
                        'requestId': str(uuid4())
                    },
                    json={
                        "privateIpGoogleAccess": True
                    }
                )
                if response.status_code >= 400:
                    raise ValueError("Unexpected response from Google (%d) : %s" % (response.status_code, response.text))
        blob = getblob('gs://{bucket}/regions'.format(bucket=ld_meta_bucket_for_project(self.project)))
        blob.upload_from_string("\n".join(regions))
        acl = blob.acl
        acl.all_authenticated().grant_read()
        acl.save()

    def __repr__(self):
        return '<lapdog.Gateway {}{}>'.format(
            self.namespace,
            ' ({})'.format(self.project) if self.project is not None else ''
        )
