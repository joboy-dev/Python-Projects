import requests
import os
from pathlib import Path
from dotenv import load_dotenv

class DataManager:
    '''This class is responsible for talking to the Google Sheet.'''
    
    def __init__(self):
        '''Initialization code'''
        
        BASE_DIR = Path(__file__).resolve().parent.parent.parent
        load_dotenv(os.path.join(BASE_DIR, ".env"))
        
        SHEETY_AUTH_TOKEN = os.getenv('SHEETY_AUTH_TOKEN')
        self.__sheety_endpoint = 'https://api.sheety.co/88896027d59dd2ab37182eea7de0e12f/flightDeals/prices'
        
        self.__headers = {
            'Authorization': f'Bearer {SHEETY_AUTH_TOKEN}'
        }
        
        sheety_response = requests.get(url=self.__sheety_endpoint, headers=self.__headers)
        
        output = sheety_response.json()
        
        self.city_data = output['prices']
      
        
    def update_iata_code(self, city_id, iata_code):
        '''Function to update all iata codes in the google sheets'''
        
        sheety_data = {
            'price': {
                'iataCode': iata_code
            }
        }
        
        sheety_update_response = requests.put(url=f'{self.__sheety_endpoint}/{city_id}', headers=self.__headers, json=sheety_data)
        sheety_update_response.raise_for_status()
        
        # print(sheety_update_response.text)
        
        
        