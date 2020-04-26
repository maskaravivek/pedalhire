from ..constants.global_constants import COMMON_PREFIX
from ..utils.api import handle_response
from flask import Blueprint
from ..services.report_service import generate_report

report_api = Blueprint('report', __name__)

@report_api.route(COMMON_PREFIX + "/generateReport", methods=['POST'])
def report():
    merchants = generate_report()
    return handle_response(merchants)
