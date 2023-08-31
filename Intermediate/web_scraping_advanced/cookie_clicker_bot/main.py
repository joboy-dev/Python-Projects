from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchDriverException
import time

current_time = time.time()
timeout = current_time + 60*5  # 5 minutes from now

process = True

try:
    driver = webdriver.Chrome()

    driver.get('http://orteil.dashnet.org/experiments/cookie/')

    # cookie button to click on at the start of the program
    cookie_button = driver.find_element(by=By.CSS_SELECTOR, value='#cookie')

    # variable to hold all the clickable action buttons
    # action_buttons = driver.find_elements(by=By.CSS_SELECTOR, value='#store div')[0:8]

    while process:
        # click on button
        cookie_button.click()
        
        # time.sleep(0.1)

        # every 5 seconds click on an action button to increase cookie productivity
        if time.time() - current_time >= 5:
            action_buttons = driver.find_elements(by=By.CSS_SELECTOR, value='#store div')[0:8]
            
            # get all the cookie currency values and store as a list
            money_elements = driver.find_elements(by=By.CSS_SELECTOR, value='#store div b')[0:8]
            currency_list = [int(money.text.split('-')[1].strip().replace(',', '')) for money in money_elements]
            
            # create a dictionary to store the price of upgrade as key and the button web element to click on as a value
            # cookie_upgrades = {
            #     currency_list[i]: action_buttons[i] for i in range(len(currency_list))
            # }
            
            # store amount of cookies gotten
            cookie_money_text = driver.find_element(by=By.CSS_SELECTOR, value='#money').text
            if ',' in cookie_money_text:
                cookie_money_value = int(cookie_money_text.replace(',', ''))
            else:
                cookie_money_value = int(cookie_money_text)
            
            # loop through the currency list from the back so as to get hold of the first action button that has the max amount of cookies that can be afforded
            for currency in currency_list[::-1]:
                if currency >= cookie_money_value:
                    action_buttons = driver.find_elements(by=By.CSS_SELECTOR, value='#store div')[0:8]
                    
                    action_buttons[currency_list.index(currency)].click()
                    
            current_time = time.time()
                    
        # check if time for program to run has been exceeded
        if current_time >= timeout:
            # cookies per second text
            cookies_per_second = driver.find_element(by=By.CSS_SELECTOR, value='#cps').text
            print(cookies_per_second)
            process = False

    driver.close()
    
except NoSuchDriverException:
    print('Connect to the internet')