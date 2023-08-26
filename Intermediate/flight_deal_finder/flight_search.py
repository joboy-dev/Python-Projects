import requests
import os
from pathlib import Path
from dotenv import load_dotenv

class FlightSearch:
    '''This class is responsible for talking to the Flight Search API'''
    
    def __init__(self, city_name):
        '''Initialization code'''
        
        BASE_DIR = Path(__file__).resolve().parent.parent.parent

        load_dotenv(os.path.join(BASE_DIR, ".env"))
        
        TEQUILA_API_KEY = os.getenv('TEQUILA_API_KEY')
        self.__tequila_endpoint = 'https://api.tequila.kiwi.com/locations/query'
        
        self.__parameters = {
            'term': city_name
        }
        
        self.__headers = {
            'apikey': TEQUILA_API_KEY,
        }
        
    
    def run_flight_search(self):
        tequila_response = requests.get(url=self.__tequila_endpoint, params=self.__parameters, headers=self.__headers)
        tequila_response.raise_for_status()
        
        output = tequila_response.json()
        
        # get iata code
        iataCode = output['locations'][0]['code']
        
        return iataCode
        
        