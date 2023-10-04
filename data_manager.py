import requests
from dotenv import  load_dotenv
import os

from users_sheety import MyNAME, PasswordSHEETY

load_dotenv()
SHEETY_ENDPOINT = os.getenv('SHEETY_ENDPOINT')
endpoint = os.getenv('endpoint')
sheety_adding = os.getenv('sheety_adding')

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        responce = requests.get(url=SHEETY_ENDPOINT,auth=(MyNAME,PasswordSHEETY))
        data = responce.json()
        self.destination_data = data['sheet1']
        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            par = {
                'term': f"{city['destination']}",
            }
            header = {
                'apikey': os.getenv('APIKAY'),
            }
            twiko_responce = requests.get(url=endpoint, params=par, headers=header)
            code_city = twiko_responce.json()['locations'][0]['code']
            shet_adding = f"sheety_adding{city['id']}"
            shet_par = {
                "sheet1": {
                }
            }
            shet_par['sheet1']['iataCode'] = code_city
            requests.put(url=shet_adding, json=shet_par,auth=(MyNAME,PasswordSHEETY))
