from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from private import password
import smtplib


class Sender:
    def __init__(self, email):
        self.email = email
        self.__message = MIMEMultipart()

    def set_info(self, sender, subject):
        self.__message = MIMEMultipart()
        self.__message['from'] = sender
        self.__message["to"] = self.email
        self.__message['subject'] = subject

    def attach_file(self, filepath, name):
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(filepath, 'rb').read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        f'attachment; filename="{name}"')
        self.__message.attach(part)

    def attach_body(self, body):
        self.__message.attach(
            MIMEText(body))

    def send_email(self):
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login('syedrizvi2023@gmail.com', password)
            smtp.send_message(self.__message)
            print('Email Sent')
