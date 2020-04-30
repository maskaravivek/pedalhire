from ..constants.global_constants import COMMON_PREFIX
from ..utils.api import handle_response
from flask import Blueprint
from ..services.report_service import generate_status_report, broadcast_emails

report_api = Blueprint('report', __name__)

@report_api.route(COMMON_PREFIX + "/generateMerchantReports", methods=['GET', 'POST'])
def report():
    generate_status_report()
    return handle_response({})


@report_api.route(COMMON_PREFIX + "/broadcastEmails", methods=['GET', 'POST'])
def broadcast():
    broadcast_emails()
    return handle_response({})
