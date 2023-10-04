import smtplib
import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

from users_sheety import MyNAME, PasswordSHEETY

load_dotenv()
account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')
TWILIO_VIRTUAL_NUMBER = os.getenv('TWILIO_VIRTUAL_NUMBER')
TWILIO_VERIFIED_NUMBER = os.getenv('TWILIO_VERIFIED_NUMBER')
USER_ENDPOINT = os.getenv('USER_ENDPOINT')
My_email = os.getenv('My_email')
PASSWORD = os.getenv('PASSWORD')

class NotificationManager:

    def send_massage(self,massage):
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=massage,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
        )
        print(message.status)


    def send_email(self,massage):

        responce = requests.get(url=USER_ENDPOINT,auth=(MyNAME,PasswordSHEETY))

        for person in responce.json()['users']:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=My_email, password=PASSWORD)

                connection.sendmail(My_email, person['email'], massage)
