import datetime
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

flight_search = FlightSearch()
massag = NotificationManager()


today_day = datetime.datetime.now()
six_month_from_today = datetime.datetime.now() + datetime.timedelta(days=(6 * 30))
start_point = 'TAL'

for city in sheet_data:
    flight = flight_search.check_flight(start_point, city['iataCode'], today_day, six_month_from_today)
    if flight == None:
        continue
    elif flight.price < city['price']:
        massage = f"Low Price alert! Only {flight.price} to fly from London-{start_point} to {flight.destination_city}-{flight.destination_airport}"
        f'from {flight.out_date} to {flight.return_date}'

        if flight.stop_overs>0:
            massage += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        # massag.send_massage( massage)
        massag.send_email(massage)