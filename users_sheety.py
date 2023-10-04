import os
import requests

USER_ENDPOINT = os.getenv('USER_ENDPOINT')
MyNAME = os.getenv('MyNAME')
PasswordSHEETY = os.getenv('PasswordSHEETY')
print("Welcome to the Anna's Flight CLub")
name = input('What is your name?\n')
last_name = input('What is your last name?\n')
email = input('What is your email?\n')
repeat_email = input('Type your email again.\n')

if email == repeat_email:
    print('Succes! Ypur email was added ,look forward')

    data = {
        'user': {
        }
    }

    data['user']['firstName'] = name
    data['user']['lastName'] = last_name
    data['user']['email'] = email
    response = requests.post(url=USER_ENDPOINT, json=data,auth=(MyNAME,PasswordSHEETY))
    print(response.text)