import os
try:
    from . import utils
except ImportError:
    import sys
    sys.path.append(os.path.dirname(__file__))
    import utils
import json
from urllib.parse import quote
import traceback

@utils.cors('DELETE')
def abort_submission(request):
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
                401
            )

        # 3) Check that submission.json exists, and is less than 1 Gib

        if 'submission_id' not in data:
            return (
                {
                    'error': 'Bad Request',
                    'message': 'Missing required parameter "submission_id"'
                },
                400
            )

        submission = utils.fetch_submission_blob(session, data['bucket'], data['submission_id'])

        result, message = utils.validate_submission_file(submission)
        if not result:
            return (
                {
                    'error': 'Bad Submission',
                    'message': message
                },
                400
            )

        # 4) Download submission and parse operation

        try:
            submission = json.loads(submission.download_as_string().decode())
        except:
            return (
                {
                    'error': 'Invalid Submission',
                    'message': 'Submission was not valid JSON'
                },
                400
            )

        if 'operation' not in submission:
            return (
                {
                    'error': 'Invalid Submission',
                    'message': 'Submission contained no operation metadata'
                },
                400
            )

        signature_blob = utils.getblob(
            'gs://{bucket}/lapdog-executions/{submission_id}/signature'.format(
                bucket=data['bucket'],
                submission_id=data['submission_id']
            ),
            credentials=session.credentials
        )
        if not signature_blob.exists():
            return (
                {
                    'error': 'No Signature',
                    'message': 'The submission signature could not be found. Refusing to abort job'
                },
                403
            )

        if not utils.verify_signature(signature_blob, (data['submission_id'] + submission['operation']).encode()):
            return (
                {
                    'error': 'Invalid Signature',
                    'message': 'Could not validate submission signature. Refusing to abort job'
                },
                403
            )

        core_session = utils.generate_core_session()

        # 5) Generate abort key

        logger.log(
            "Generating new signature",
            data=data['submission_id']
        )

        utils.sign_object(
            data['submission_id'].encode(),
            utils.getblob(
                'gs://{bucket}/lapdog-executions/{submission_id}/abort-key'.format(
                    bucket=data['bucket'],
                    submission_id=data['submission_id']
                ),
                credentials=session.credentials
            ),
            core_session.credentials
        )

        if 'hard' in data and data['hard']:
            # 6) Abort operation
            logger.log(
                "Hard-aborting submission",
                submission_id=data['submission_id'],
                operation_id=submission['operation'],
                severity='NOTICE'
            )
            response = core_session.post(
                "https://genomics.googleapis.com/v2alpha1/{operation}:cancel".format(
                    operation=quote(submission['operation']) # Do not quote slashes here
                )
            )

            return response.text, response.status_code
        return (
            {
                'status': 'Aborting',
                'message': 'A soft-abort request has been sent.'
                ' If the submission does not abort soon, abort it with hard=True to force-kill the cromwell server'
            },
            200
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
