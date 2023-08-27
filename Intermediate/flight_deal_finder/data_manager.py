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
        
        self.__headers = {
            'Authorization': f'Bearer {SHEETY_AUTH_TOKEN}'
        }
        
        # -------------------- PRICES ---------------------- #
        
        self.__sheety_prices_endpoint = 'https://api.sheety.co/88896027d59dd2ab37182eea7de0e12f/flightDeals/prices'
        
        try:
            sheety_prices_response = requests.get(url=self.__sheety_prices_endpoint, headers=self.__headers)
            prices_output = sheety_prices_response.json()
            
            # get the list of all cities and their data
            self.city_data = prices_output['prices']
            # print(self.city_data)
        except requests.exceptions.ConnectionError as e:
            print(e)
            print('Ensure you are connected to the internet\n\n')
        
        # -------------------- USERS ----------------------- #
        
        try:
            self.__sheety_users_endpoint = 'https://api.sheety.co/88896027d59dd2ab37182eea7de0e12f/flightDeals/users'
            sheety_users_response = requests.get(url=self.__sheety_users_endpoint, headers=self.__headers)
            users_output = sheety_users_response.json()
            
            # get the list of all users and their data
            self.users = users_output['users']
        except requests.exceptions.ConnectionError as e:
            print(e)
            print('Ensure you are connected to the internet\n\n')
        
      
        
    def update_iata_code(self, city_id, iata_code):
        '''Function to update all iata codes in the google sheets'''
        
        sheety_data = {
            'price': {
                'iataCode': iata_code
            }
        }
        
        try:
            sheety_update_response = requests.put(url=f'{self.__sheety_prices_endpoint}/{city_id}', headers=self.__headers, json=sheety_data)
            sheety_update_response.raise_for_status()
            
            # print(sheety_update_response.text)
        except requests.exceptions.ConnectionError as e:
            print(e)
            print('Ensure you are connected to the internet\n\n')
        
        
    def add_new_users(self, first_name, last_name, email):
        '''Function to add new user to the google sheets'''
        
        sheety_data = {
            'user': {
                'firstName': first_name,
                'lastName': last_name,
                'email': email
            }
        }
        
        try:
            sheety_add_response = requests.post(url=f'{self.__sheety_users_endpoint}', headers=self.__headers, json=sheety_data)
            sheety_add_response.raise_for_status()
        except requests.exceptions.ConnectionError as e:
            print(e)
            print('Ensure you are connected to the internet\n\n')
        
        