from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *
from urllib.request import HTTPError
import os
import python_http_client
from ..constants.env_constants import SUPPORT_EMAIL, SEND_GRID_API_KEY

def send_email_with_template(email, subject, template, params):
    message = Mail(
        from_email=From(SUPPORT_EMAIL, 'PedalHire'),
        to_emails=To(email, email),
        subject=Subject(subject)
    )

    message.template_id = TemplateId(template)
    message.dynamic_template_data = params
    send_email(message)

def send_email_with_html(email, subject, html_content):
    message = Mail(
        from_email=From(SUPPORT_EMAIL, 'PedalHire'),
        to_emails=To(email, email),
        subject=Subject(subject),
        html_content=html_content
    )

    send_email(message)

def send_email(message):
    sg = SendGridAPIClient(SEND_GRID_API_KEY)
    try:
        response = sg.send(message)
    except (HTTPError, python_http_client.exceptions.BadRequestsError) as error:
        print(str(error.body), flush=True)
