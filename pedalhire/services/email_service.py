from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *
from urllib.request import HTTPError
import os
import python_http_client

# https://github.com/sendgrid/sendgrid-python/blob/master/use_cases/kitchen_sink.md
def send_request_approval_email(user_id, role_id, role_type, data):

    send_email_with_template(
        email=os.environ['SUPPORT_EMAIL'],
        subject='Verification Request',
        template='d-33daa8f03c0f45f6af01022a6eacf259',
        params={
            'name': data['name'],
            'user_id': str(user_id),
            'role_type': role_type,
            'role_id': str(role_id),
            'email': data['email'],
            'phone_number': data['poc_contact_number'],
            'address': data['address'],
            'city': data['city'],
            'state': data['state'],
            'zip': data['location'],
            'sterization_method': ', '.join(data['sterilization_method'])
        }
    )

def send_email_with_template(email, subject, template, params):
    message = Mail(
        from_email=From(os.environ['SUPPORT_EMAIL'], 'Luminosity Support'),
        to_emails=To(email, email),
        subject=Subject(subject)
    )

    message.template_id = TemplateId(template)
    message.dynamic_template_data = params
    send_email(message)

def send_email_with_html(email, subject, html_content):
    message = Mail(
        from_email=From(os.environ['SUPPORT_EMAIL'], 'Luminosity Support'),
        to_emails=To(email, email),
        subject=Subject(subject),
        html_content=html_content
    )

    send_email(message)

def send_email(message):
    # Move to os.environ.get('SENDGRID_API_KEY') at some point
    sg = SendGridAPIClient('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')
    try:
        response = sg.send(message)
    except (HTTPError, python_http_client.exceptions.BadRequestsError) as error:
        print(str(error.body), flush=True)
