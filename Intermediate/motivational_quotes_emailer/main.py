import smtplib
import datetime as dt
import random

MY_EMAIL = 'devjoboy@gmail.com'
PASSWORD = 'jdeasnpdzvzwjqqw'

# work with date
now = dt.datetime.now()
# get weekday
weekday = now.weekday()

# check if weekday is Monday
if weekday == 0:
    # open quotes file
    with open('Intermediate/motivational_quotes_emailer/quotes.txt', 'r') as quotes_file:
        quotes = quotes_file.readlines()
        random_quote = random.choice(quotes)
        print(random_quote)
    
    # open a connection
    with smtplib.SMTP('smtp.gmail.com') as conn:
        conn.starttls()
        conn.login(user=MY_EMAIL, password=PASSWORD)
        conn.sendmail(from_addr=MY_EMAIL, to_addrs='devtesting941@gmail.com', msg=f'Subject: Monday Motivation\n\nHere is a little dose of Monday motivation.\n\n{random_quote}\n\nHang in there. You can do it!!')