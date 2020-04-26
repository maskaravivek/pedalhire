from flask import Blueprint
from ..constants.global_constants import COMMON_PREFIX
from ..utils.api import handle_response

health_check_api = Blueprint('health_check', __name__)

@health_check_api.route(COMMON_PREFIX + "/status")
def check_health():
    return handle_response({ "status": "healthy" })
