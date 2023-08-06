# This module defines utilities for the cloud function api

from .utils import __API_VERSION__, generate_default_session
import tempfile
import shutil
import subprocess
import glob
import os
import json
import time

__FUNCTION_MAPPING__ = {
    'create_submission': 'submit.py',
    'abort_submission': 'abort.py',
    'existence': 'internal.py',
    'redacted': 'internal.py',
    'check_abort': 'internal.py',
    'quotas': 'quotas.py',
    'register': 'register.py',
    'query_account': 'query.py',
    'insert_resolution': 'resolution.py',
    'webhook': 'webhook.py',
    'update': 'webhook.py',
    'oauth': 'auth.py'
}

RESOLUTION_URL = "https://us-central1-a-graubert.cloudfunctions.net/resolve-" + __API_VERSION__['resolve']

def __autodeploy_internal(endpoint, namespace):
    from lapdog.gateway import resolve_project_for_namespace
    from lapdog.cloud.patch import __ENDPOINTS__ as endpoint_map
    project = resolve_project_for_namespace(namespace)
    service_account = 'lapdog-functions@{}.iam.gserviceaccount.com'.format(project)
    function = endpoint_map[endpoint]
    print("Deploying", function, '@', __FUNCTION_MAPPING__[function], '->', endpoint)
    print(service_account, 'in', namespace, '(', project,')')
    input()
    _deploy(function, endpoint, service_account, project)

def _deploy(function, endpoint, service_account=None, project=None, overload_version=None):
    if overload_version is None:
        overload_version = __API_VERSION__[endpoint]
    with tempfile.TemporaryDirectory() as tempdir:
        with open(os.path.join(tempdir, 'requirements.txt'), 'w') as w:
            w.write('google-auth==1.6.3\n')
            w.write('google-cloud-storage==1.20.0\n')
            w.write('google-cloud-kms==1.2.1\n')
            w.write('cryptography==2.7\n')
            w.write('google-cloud-logging==1.12.1\n')
            w.write('google-cloud-core==1.0.3\n')
        shutil.copyfile(
            os.path.join(
                os.path.dirname(__file__),
                __FUNCTION_MAPPING__[function]
            ),
            os.path.join(tempdir, 'main.py')
        )
        shutil.copyfile(
            os.path.join(
                os.path.dirname(__file__),
                'utils.py'
            ),
            os.path.join(tempdir, 'utils.py')
        )
        cmd = 'gcloud {project} functions deploy {endpoint}-{version} --entry-point {function} --runtime python37 --trigger-http --allow-unauthenticated --source {path} {service_account}'.format(
            endpoint=endpoint,
            version=overload_version,
            function=function,
            path=tempdir,
            service_account='' if service_account is None else ('--service-account '+service_account),
            project='' if project is None else ('--project '+project)
        )
        print(cmd)
        subprocess.check_call(
            cmd,
            shell=True,
            executable='/bin/bash'
        )
        time.sleep(5) # Give the API a brief chance to catch up to the deployment
        session = generate_default_session()
        policy = session.get(
            'https://cloudfunctions.googleapis.com/v1/projects/{}/locations/us-central1/functions/{}-{}:getIamPolicy'.format(
                project if project is not None else session._default_project,
                endpoint,
                overload_version
            )
        ).json()
        print(policy)
        found = False
        for i, binding in enumerate(policy['bindings']):
            if binding['role'] == 'roles/cloudfunctions.invoker':
                found = True
                policy['bindings'][i]['members'].append('allAuthenticatedUsers')
        if not found:
            policy['bindings'].append({
                'role': 'roles/cloudfunctions.invoker',
                'members': ['allAuthenticatedUsers']
            })
        session.post(
            'https://cloudfunctions.googleapis.com/v1/projects/{}/locations/us-central1/functions/{}-{}:setIamPolicy'.format(
                project if project is not None else session._default_project,
                endpoint,
                overload_version
            ),
            headers={'Content-Type': 'application/json'},
            json={
                'policy': policy,
                'updateMask': 'bindings'
            }
        )

def __generate_alert_internal(title, alert_type, content, text=None):
    """
    You're welcome to use this function, but you won't have permissions
    """
    assert alert_type in {'critical', 'warning', 'info'}
    blob = utils.getblob(
        'gs://lapdog-alerts/{}'.format(title)
    )
    alert = {
        'type': alert_type,
        'content': content
    }
    if text is not None:
        alert['text'] = text
    blob.upload_from_string(json.dumps(alert))
