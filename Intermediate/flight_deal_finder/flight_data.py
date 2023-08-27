import requests
import os
from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime
from dateutil.relativedelta import relativedelta

class FlightData:
    '''This class is responsible for structuring the flight data.'''
    
    def __init__(self, destination_iata):
        '''Initialization code'''
        
        BASE_DIR = Path(__file__).resolve().parent.parent.parent

        load_dotenv(os.path.join(BASE_DIR, ".env"))
        
        TEQUILA_API_KEY = os.getenv('TEQUILA_API_KEY')
        self.__tequila_search_endpoint = 'https://api.tequila.kiwi.com/v2/search'
        
        CURRENT_LOCATION_IATA = 'LON'
        
        # ------------- USING DATETIME MODULE ----------------- #
        today = datetime.now().date()
        
        tomorrow = (today + relativedelta(days=1)).strftime('%d/%m/%Y')
        six_months = (today + relativedelta(months=6)).strftime('%d/%m/%Y')
        seven_days = (today + relativedelta(days=7)).strftime('%d/%m/%Y')
        twenty_eight_days = (today + relativedelta(days=28)).strftime('%d/%m/%Y')
        
        # print(tomorrow)
        # print(urllib.parse.quote(twenty_eight_days))
        
        self.__parameters = {
            'fly_from': CURRENT_LOCATION_IATA,
            'fly_to': destination_iata,
            'date_from': tomorrow,
            'date_to': six_months,
            'return_from': seven_days,
            'return_to': twenty_eight_days,
            'curr': 'GBP'
        }
        
        self.__headers = {
            'apikey': TEQUILA_API_KEY,
        }
        
        
    def get_flight_data(self):
        '''Function to get all necessary flight data'''
        
        try:
            tequila_search_response = requests.get(url=self.__tequila_search_endpoint, params=self.__parameters, headers=self.__headers)
            # print(tequila_search_response)
            tequila_search_response.raise_for_status()
            
            output = tequila_search_response.json()
            # print(output)
            
            # get all flight details for all flights and store in a variable
            all_flights = output['data']
            # print(len(self.all_flights))
            
            return all_flights
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            print("Response content:", tequila_search_response.content)
        except requests.exceptions.ConnectionError as e:
            print(e)
            print('Ensure you are connected to the internet')