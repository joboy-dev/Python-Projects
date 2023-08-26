import os
from pathlib import Path
from dotenv import load_dotenv
import smtplib

class NotificationManager:
    '''This class is responsible for sending notifications with the deal flight details.'''
    
    def __init__(self):
        '''Initialization code'''
        
        BASE_DIR = Path(__file__).resolve().parent.parent.parent

        load_dotenv(os.path.join(BASE_DIR, ".env"))
        
        self.__EMAIL = os.getenv('MY_EMAIL')
        self.__PASSWORD = os.getenv('PASSWORD')
        
    
    def send_notification(self, flight_budget, min_flight_price, message):
        '''Function to send notification about a cheap flight'''
        
        # check if cheapest flight rice is within your flight budget
        if min_flight_price <= flight_budget:
            with smtplib.SMTP('smtp.gmail.com') as conn:
                conn.starttls()
                conn.login(user=self.__EMAIL, password=self.__PASSWORD)
                
                conn.sendmail(from_addr=self.__EMAIL, to_addrs='devtesting941@gmail.com', msg=message)