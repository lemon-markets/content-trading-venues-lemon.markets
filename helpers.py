import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class EmailSenderSendgrid:
    def __init__(self, mail_text: str, mail_subject: str):
        load_dotenv()
        message = Mail(
            from_email=os.environ.get('EMAIL_FROM'),
            to_emails=os.environ.get('EMAIL_TO'),
            subject=mail_subject,
            html_content=mail_text)
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print('Email successfully delivered')
        except Exception as e:
            print(e)
