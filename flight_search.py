import os
from dotenv import load_dotenv
from pprint import pprint
from flight_data import FlightData
import requests

load_dotenv()
endpoint = os.getenv('endpoint_flight')
TEQUILA_KEY = os.getenv('TEQUILA_KEY')


class FlightSearch:

    def check_flight(self, original_city, destination, time_togo, return_time):
        headers = {
            'apikey': TEQUILA_KEY,
        }
        param = {
            "adults": 1,
            'fly_from': original_city,
            'fly_to': destination,
            'date_from ': time_togo.strftime("%d/%m/%Y"),
            'date_to': return_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR"
        }

        responce = requests.get(url=endpoint, params=param, headers=headers)

        try:
            data = responce.json()['data'][0]

        except IndexError:
            param["max_stopovers"] = 2
            responce = requests.get(url=endpoint, params=param, headers=headers)
            pprint(responce)
            data = responce.json()['data'][0]
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data

        flight_data = FlightData(
            price=data['price'],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]

        )
        return flight_data
