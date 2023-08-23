import requests
from datetime import datetime
import smtplib
import time

def iss_overhead():
    '''Function to check if the ISS is close'''
    
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    print(data)


    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT-5 <= iss_latitude <= MY_LAT+5) and (MY_LONG-5 <= iss_longitude <= MY_LONG+5):
        return True
    else:
        return False
    
def is_night():
    '''Function to check if it's night time'''
    
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    now = datetime.now()

    print(sunset)
    
    if now.hour >= sunset or now.hour <= sunrise:
        return True
    else:
        return False
    

while True:
    MY_LAT = 51.507351 # Your latitude
    MY_LONG = -0.127758 # Your longitude

    MY_EMAIL = 'devjoboy@gmail.com'
    PASSWORD = 'jdeasnpdzvzwjqqw'
    
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    if iss_overhead() and is_night():
        with smtplib.SMTP('smtp.gmail.com') as conn:
            conn.starttls()
            conn.login(user=MY_EMAIL, password=PASSWORD)
            conn.sendmail(from_addr=MY_EMAIL, to_addrs='devtesting941@gmail.com', msg=f"Subject: The International Space Station.\n\nThe International Space Station is close to you.\n\nLook up.")
    
    # sleep for 60 seconds before the code runs again
    time.sleep(60)