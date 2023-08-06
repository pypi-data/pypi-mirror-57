import os
try:
    from . import utils
except ImportError:
    import sys
    sys.path.append(os.path.dirname(__file__))
    import utils
import base64
import traceback

@utils.cors("POST")
def check_abort(request):
    logger = utils.CloudLogger().log_request(request)
    try:
        data = request.get_json()
        if not isinstance(data, dict):
            return "No Data", 400
        if not ('key' in data and 'id' in data):
            return "missing params", 400
        if utils.verify_signature(base64.b64decode(data['key'].encode()), data['id'].encode(), _is_blob=False):
            return 'OK', 200
        return 'ERROR', 400
    except:
        logger.log_exception()
        return (
            {
                'error': 'Unknown Error',
                'message': traceback.format_exc()
            },
            500
        )

@utils.cors('GET')
def existence(request):
    utils.CloudLogger().log_request(request)
    return 'OK', 200

@utils.cors("GET", "PATCH", "PUT", "POST", "DELETE")
def redacted(request):
    """
    This will get deployed to deleted endpoints to redact them.
    This will allow older clients to get notified of updated API versions
    """
    utils.CloudLogger().log_request(request)
    return {
        'error': "Endpoint Redacted",
        'message': (
            "This endpoint has been disabled for security reasons."
            " Please upgrade to the latest version of Lapdog to access updated endpoints"
        )
    }, 410
