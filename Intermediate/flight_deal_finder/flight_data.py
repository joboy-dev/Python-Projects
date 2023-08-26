import requests
import os
from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime
from dateutil.relativedelta import relativedelta
import urllib.parse

# from flight_search import FlightSearch

class FlightData:
    '''This class is responsible for structuring the flight data.'''
    
    def __init__(self, destination_iata):
        '''Initialization code'''
        
        BASE_DIR = Path(__file__).resolve().parent.parent.parent

        load_dotenv(os.path.join(BASE_DIR, ".env"))
        
        TEQUILA_API_KEY = os.getenv('TEQUILA_API_KEY')
        __tequila_search_endpoint = 'https://api.tequila.kiwi.com/v2/search'
        
        CURRENT_LOCATION_IATA = 'LON'
        
        # ------------- USING DATETIME MODULE ----------------- #
        today = datetime.now().date()
        
        # six_months = today + timedelta(days=6*30)
        
        tomorrow = (today + relativedelta(days=1)).strftime('%d/%m/%Y')
        six_months = (today + relativedelta(months=6)).strftime('%d/%m/%Y')
        seven_days = (today + relativedelta(days=7)).strftime('%d/%m/%Y')
        twenty_eight_days = (today + relativedelta(days=28)).strftime('%d/%m/%Y')
        
        # print(tomorrow)
        # print(urllib.parse.quote(twenty_eight_days))
        
        __parameters = {
            'fly_from': CURRENT_LOCATION_IATA,
            'fly_to': destination_iata,
            'date_from': urllib.parse.quote(tomorrow),
            'date_to': urllib.parse.quote(six_months),
            'return_from': urllib.parse.quote(seven_days),
            'return_to': urllib.parse.quote(twenty_eight_days),
            'curr': 'GBP'
        }
        
        __headers = {
            'apikey': TEQUILA_API_KEY,
        }
        
        try:
            tequila_search_response = requests.get(url=__tequila_search_endpoint, params=__parameters, headers=__headers)
            # print(tequila_search_response)
            tequila_search_response.raise_for_status()
            
            output = tequila_search_response.json()
            # print(output)
            
            # get all flight details for all flights and store in a variable
            self.all_flights = output['data']
            # print(len(self.all_flights))
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            print("Response content:", tequila_search_response.content)