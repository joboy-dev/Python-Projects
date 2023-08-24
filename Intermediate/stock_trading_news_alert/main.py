import requests
import smtplib
from email.mime.text import MIMEText
import datetime as dt
from dateutil.relativedelta import relativedelta
import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(os.path.join(BASE_DIR, ".env"))

MY_EMAIL = os.getenv('MY_EMAIL')
PASSWORD = os.getenv('PASSWORD')

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# ----------------------- STOCK API-------------------------- #

STOCK_PRICE_API_KEY = os.getenv('STOCK_PRICE_API_KEY')
stock_price_api = 'https://www.alphavantage.co/query?'

stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': STOCK_PRICE_API_KEY
}

stock_api_response = requests.get(stock_price_api, params=stock_params)

# store stock data in variable
stock_data = stock_api_response.json()

# -------------------------- DATE --------------------------- #

# get today's date
today = dt.datetime.now().date()

# get the dates fot last two days each
yesterday_date = str(today - relativedelta(days=1))
day_before_yesterday_date = str(today - relativedelta(days=2))


# ---------------------- NEWS API---------------------------- #
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
news_api = 'https://newsapi.org/v2/everything'

news_api_params = {
    'q': 'tesla',
    'from': yesterday_date,
    'sortBy': 'publishedAt',
    'apiKey': NEWS_API_KEY
}

news_api_response = requests.get(news_api, params=news_api_params)

# store news data in variable
news_data = news_api_response.json()

# get first 3 articles
articles = news_data['articles'][0:2]
print(articles)

article_message = ''

for article in articles:
    article_message += f"Headline: {article['title']}\nBrief: {article['description']}\n\n"
    
print(article_message)

# ---------------------- STOCK DATA USAGE -------------------- #

# get data for yesterday stcok
yesterday_stock_data = stock_data['Time Series (Daily)'][yesterday_date]
day_before_yesterday_stock_data = stock_data['Time Series (Daily)'][day_before_yesterday_date]

# get closing price for the two days
yesterday_closing_price = float(yesterday_stock_data['4. close'])
day_before_yesterday_closing_price = float(day_before_yesterday_stock_data['4. close'])

stock_price_difference = yesterday_closing_price - day_before_yesterday_closing_price

# get percentage chang between yesterday and day before
percentage_change = int((stock_price_difference / day_before_yesterday_closing_price) * 100)

# -------------------- NEWS DATA USAGE ------------------------ #

# print(opening_message)

# convert message into utf-8 standard
# message_to_send = MIMEText(article_message, 'plain', 'utf-8')

with smtplib.SMTP('smtp.gmail.com') as conn:
    conn.starttls()
    conn.login(user=MY_EMAIL, password=PASSWORD)
    
    # if percentage_change >= 0 and percentage_change <= 5:
    #     opening_message = f'TSLA: ↑ {percentage_change}%'
    #     conn.sendmail(from_addr=MY_EMAIL, to_addrs='devtesting941@gmail.com', msg=f"Subject:    {COMPANY_NAME} Stock Price Alert\n\n{article_message}")
    # elif percentage_change < 0 and percentage_change >= -5:
    #     opening_message = f'TSLA: ↓ {abs(percentage_change)}%'
    #     conn.sendmail(from_addr=MY_EMAIL, to_addrs='devtesting941@gmail.com', msg=f"Subject:{COMPANY_NAME} Stock Price Alert\n\n{article_message}")
    
    conn.sendmail(from_addr=MY_EMAIL, to_addrs='devtesting941@gmail.com', msg=f"Subject:{COMPANY_NAME} Stock Price Alert\n\n{article_message}")


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

