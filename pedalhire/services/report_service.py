from .merchant_service import get_all_merchants
from .email_service import send_email_with_template
from ..utils.json_to_csv import convert_json_to_csv
from .upload_service import upload_blob
from ..constants.env_constants import SUPPORT_EMAIL
import uuid


def generate_report():
    merchants = get_all_merchants()
    merchant_json = {
        "merchants": merchants
    }

    report_file_name = str(uuid.uuid4())+'.csv'
    convert_json_to_csv('merchants', merchant_json, '/tmp/' + report_file_name)
    upload_blob('/tmp/' + report_file_name, report_file_name)

    report_link = 'https://storage.cloud.google.com/pedalhire/{}'.format(
        report_file_name)
    send_email_with_template(SUPPORT_EMAIL, 'Report Generated',
                             'd-760c6f23a12740d8bb3b66c09c9f27c5', {'report_link': report_link})
    return merchant_json
