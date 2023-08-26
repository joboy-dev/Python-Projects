from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_mamager = DataManager()

# get all cities and their data
sheet_data = data_mamager.city_data

for city in sheet_data:
    city_iata_code = city['iataCode']
    city_name = city['city']
    
    # check if city iata code fild is empty
    if len(city_iata_code) == 0:
        # pass each city name to the FlightSearch class
        flight_search = FlightSearch(city_name=city_name)
        iata_code = flight_search.run_flight_search()
        
        # update google sheets iata code values from data manager class
        data_mamager.update_iata_code(city_id=city['id'], iata_code=iata_code)
    
    flight_data = FlightData(destination_iata=city['iataCode'])
    
    # get all the flights for each city
    flight_list = flight_data.all_flights
    
    # I noticed that the flights are arranged in order of cost so the least priced flight will be the first element
    least_priced_flight = flight_list[0]
    min_price = least_priced_flight['price']
    
    # get all relevant data from the cheapest flight data to use in sending notifications
    city_from = least_priced_flight['cityFrom']
    fly_from = least_priced_flight['flyFrom']
    city_to = least_priced_flight['cityTo']
    fly_to = least_priced_flight['flyTo']
    outbound_date = least_priced_flight['route'][0]['local_departure'].split('T')[0]
    inbound_date =  least_priced_flight['route'][1]['local_departure'].split('T')[0]
    
    # message to send
    message = f"Subject: Flight Price Alert\n\nLow price alert!\nOnly {min_price} GBP to fly from {city_from}-{fly_from} to {city_to}-{fly_to}, from {outbound_date} to {inbound_date}"
    
    notification_manager = NotificationManager()
    # send notification
    notification_manager.send_notification(flight_budget=city['lowestPrice'], min_flight_price=min_price, message=message)
    
    
    
    # print(least_priced_flight)
    
    # print(f'{city_name}: {min_price}')

    
    # ------------------------------------------------------ #
    # ------------------------------------------------------ #
    # ------------------------------------------------------ #
    
    # THIS WAY WORKS ALSO BUT IT WILL ONLY GET THE MINIMUM FLIGHT PRICE....ACCESS TO OTHER ELEMENTS NEEDED FOR SENDING NOTIFICATIONS WILL BE RESTRICTED
    
    # flight_prices = {}
    
    # # store all the flight prices in a dictionary where the key is the city to travel to
    # flight_prices[city_name] = [flight_list[flight_no]['price'] for flight_no in range(len(flight_list))]
    
    # min_flight_price = min(flight_prices[city_name])
    
