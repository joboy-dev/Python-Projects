import smtplib
import datetime as dt
import random
import pandas as pd
import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
# print(BASE_DIR)

load_dotenv(os.path.join(BASE_DIR, ".env"))

MY_EMAIL = os.getenv('MY_EMAIL')
PASSWORD = os.getenv('PASSWORD')

birthday_data = pd.read_csv('birthdays.csv')
birthdays = birthday_data.to_dict(orient='records')

now = dt.datetime.now()
day = now.day
month = now.month

for birthday in birthdays:
    if birthday['month'] == month and birthday['day'] == day:
        # print(birthday)
        random_letter_no = random.randint(1, 3)
        
        with open(f'letter_templates/letter_{random_letter_no}.txt') as birthday_letter:
            letter = birthday_letter.read()
            
            letter_to_send = letter.replace('[NAME]', birthday['name'])
            
            # print(letter_to_send)
            
            try:
                # open connection
                with smtplib.SMTP('smtp.gmail.com') as conn:
                    conn.starttls()
                    conn.login(user=MY_EMAIL, password=PASSWORD)
                    conn.sendmail(from_addr=MY_EMAIL, to_addrs=birthday['email'], msg=f"Subject: Happy Birthday!!\n\n{letter_to_send}")
            except Exception as e:
                # DEBUGGING
                print(e)
                print('Connect to the Internet and try again')
    else:
        print('No birthday happening today.')