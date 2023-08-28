import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path
from pprint import pprint
import lxml
import smtplib

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

# needed for oauth to spotify
MY_EMAIL = os.getenv('MY_EMAIL')
PASSWORD = os.getenv('PASSWORD')

product_url = 'https://www.amazon.com/SAMSUNG-Smartphone-Unlocked-Brightest-Processor/dp/B09MVZ93YN/ref=sr_1_2_sspa?keywords=samsung%2Bgalaxy%2Bs21&qid=1693258405&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
    'Accept-Language': 'en-US,en;q=0.9'
}
response = requests.get(product_url, headers=headers)
data = response.text

soup = BeautifulSoup(data, 'lxml')

# get the product title
product_title_tag = soup.select_one(selector='#title #productTitle')
product_title = product_title_tag.get_text().strip()
# print(product_title)

# get the tag holding the price
price_tag = soup.select_one(selector='.a-price .a-offscreen')

price_text = price_tag.get_text()

# convert the pext into a floating point number
price_of_item = float(price_text[1:])
# print(price_of_item)

budget = price_of_item - 200
# send email if product price is less than budget
if price_of_item < budget:
    try:
        with smtplib.SMTP('smtp.gmail.com', port=587) as conn:
            print('Sending email...')
            
            conn.starttls()
            conn.login(user=MY_EMAIL, password=PASSWORD)
            conn.sendmail(from_addr=MY_EMAIL, to_addrs='devtesting941@gmail.com', msg=f"Subject: Amazon Price Alert!\n\n{product_title} ia now ${price_of_item}.\nGet it not at:\n{product_url}")
            
            print('Email sent.')
    except Exception as e:
        print(e)     
        