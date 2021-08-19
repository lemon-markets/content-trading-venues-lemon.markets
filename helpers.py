import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
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
            print('email successfully delivered')
        except Exception as e:
            print(e.message)


class RequestHandler:
    load_dotenv()
    url_data: str = os.environ.get("BASE_URL_DATA")
    url_trading: str = os.environ.get("BASE_URL_TRADING")

    def get_data_data(self, endpoint: str):
        """
        :param endpoint: {str} only append the endpoint to the base url
        :return:
        """
        response = requests.get(self.url_data + endpoint,
                                headers={
                                    "Authorization": "Bearer " + os.environ.get("TOKEN_KEY")
                                })

        return response.json()

    def get_data_trading(self, endpoint: str):
        """
        :param endpoint: {str} only append the endpoint to the base url
        :return:
        """
        response = requests.get(self.url_trading + endpoint,
                                headers={
                                    "Authorization": "Bearer "+os.environ.get("TOKEN_KEY")
                                })

        return response.json()

    def put_data(self, endpoint: str):
        response = requests.put(self.url_trading + endpoint,
                                headers={
                                    "Authorization": "Bearer " + os.environ.get("TOKEN_KEY")
                                })
        return response.json()

    def post_data(self, endpoint: str, data):
        response = requests.post(self.url_trading + endpoint,
                                 data,
                                 headers={
                                     "Authorization": "Bearer " + os.environ.get("TOKEN_KEY")
                                 })
        return response.json()
