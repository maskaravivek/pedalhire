from .merchant_service import get_merchant_updates, get_all_merchants
from .user_service import get_all_users
from .email_service import send_email_with_template
from ..utils.json_to_csv import convert_json_to_csv
from .upload_service import upload_blob
import uuid
from ..constants.env_constants import GOOGLE_CLOUD_BUCKET


def generate_status_report():
    merchants = get_all_merchants()
    for merchant in merchants:
        print(merchant['login']['email_id'])
        products_status = get_merchant_updates(merchant['login']['email_id'])
        print(get_merchant_updates(merchant['login']['email_id']))
        product_status_json = {
            "products": products_status
        }
        print(product_status_json)
        report_file_name = str(uuid.uuid4()) + '.csv'
        convert_json_to_csv('products', product_status_json, '/tmp/' + report_file_name)
        upload_blob('/tmp/' + report_file_name, report_file_name, GOOGLE_CLOUD_BUCKET)

        report_link = 'https://storage.cloud.google.com/pedalhire/{}'.format(
            report_file_name)
        send_email_with_template(merchant['login']['email_id'], 'Daily Merchant Report',
                                 'd-760c6f23a12740d8bb3b66c09c9f27c5',
                                 {'Sender_Name': merchant['first_name'] + ' ' + merchant['last_name'], 'Report_Link': report_link})

    return True

def broadcast_emails():
    users = get_all_users()
    for user in users:
        print(user['login']['email_id'])
        send_email_with_template(user['login']['email_id'], 'Daily User Report',
                                 'd-a234eee57b824f2d8745600a7724eeb6',
                                 {'Sender_Name': user['first_name'] + ' ' + user['last_name']})

    return True
