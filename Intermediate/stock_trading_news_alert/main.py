import requests
import smtplib
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
articles = news_data['articles'][0:3]
# print(articles)

article_message = ''

for article in articles:
    article_headline = article['title']
    article_body = article['description']
    
    article_message += f"Headline: {article_headline}\nBrief: {article_body}\n\n"
    
# encode article message
encoded_message = article_message.encode('utf-8')
article_message = encoded_message.decode('utf-8')

# print(encoded_message)

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
try:
    with smtplib.SMTP('smtp.gmail.com') as conn:
        conn.starttls()
        conn.login(user=MY_EMAIL, password=PASSWORD)

        if percentage_change >= 0 and percentage_change <= 5:
            opening_message = f'TSLA: ↑ {percentage_change}%'
            conn.sendmail(from_addr=MY_EMAIL, to_addrs='devtesting941@gmail.com', msg=f"Subject:    {COMPANY_NAME} Stock Price Alert\n\n{article_message}")
        elif percentage_change < 0 and percentage_change >= -5:
            opening_message = f'TSLA: ↓ {abs(percentage_change)}%'
            conn.sendmail(from_addr=MY_EMAIL, to_addrs='devtesting941@gmail.com', msg=f"Subject:{COMPANY_NAME} Stock Price Alert\n\n{article_message}")
            
except UnicodeEncodeError as e:
    print(f'ERROR: {e}')