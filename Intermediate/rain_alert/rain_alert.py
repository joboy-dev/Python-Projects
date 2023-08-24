import requests
import smtplib
import datetime as dt
import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
# print(BASE_DIR)

load_dotenv(os.path.join(BASE_DIR, ".env"))

API_KEY = os.getenv('OPEN_WEATHER_MAP_API_KEY')
# print(API_KEY)
MY_LAT = 6.586970
MY_LONG = 3.500170

api = f"https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': API_KEY,
    'exclude': 'current,minutely,daily'
}
response = requests.get(api, params=weather_params)
response.raise_for_status()

weather_data = response.json()

will_rain = False

weather_ids =[weather_data['hourly'][hour]['weather'][0]['id'] for hour in range(12)]
# print(weather_ids)

for id in weather_ids:
    if id < 700:
        will_rain = True
        
now = dt.datetime.now()
MY_EMAIL = os.getenv('MY_EMAIL')
PASSWORD = os.getenv('PASSWORD')
        
if will_rain:
    with smtplib.SMTP('smtp.gmail.com') as conn:
        conn.starttls()
        conn.login(user=MY_EMAIL, password=PASSWORD)
        conn.sendmail(from_addr=MY_EMAIL, to_addrs='devtesting941@gmail.com', msg="Subject: Rain Alert!\n\nCarry your umbrella with you as you go out today as it will rain within the next 12 hours.\n\nThank you.")
