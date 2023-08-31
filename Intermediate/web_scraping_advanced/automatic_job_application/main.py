from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

# needed for oauth to spotify
EMAIL = os.getenv('LINKEDIN_EMAIL')
PASSWORD = os.getenv('LINKEDIN_PASSWORD')

try:
    driver = webdriver.Chrome()

    url = 'https://www.linkedin.com/jobs/search/?currentJobId=3704508936&f_AL=true&f_WT=2%2C1%2C3&keywords=python%20developer&refresh=true'
    driver.get(url)

    # get sign in button 
    sign_in_button = driver.find_element(by=By.CSS_SELECTOR, value='.nav__button-secondary')
    sign_in_button.click()
    
    time.sleep(5)

    # get email and password text fields
    email_text_field = driver.find_element(by=By.ID, value='username')
    password_text_field = driver.find_element(by=By.ID, value='password')
    # type into the fields
    email_text_field.send_keys(EMAIL)
    password_text_field.send_keys(PASSWORD)

    # get next sign in button
    next_sign_in_button = driver.find_element(by=By.CSS_SELECTOR, value='.btn__primary--large')
    next_sign_in_button.click()
    
    time.sleep(20)
    
    # get list of all available jobs
    available_jobs_list = driver.find_elements(by=By.CSS_SELECTOR, value='.job-card-list__title')
    # print(len(available_jobs_list))
    time.sleep(5)
    
    for job in available_jobs_list:
        # print(job.text)
        job.click()
        time.sleep(5)
        
        save_button = driver.find_element(by=By.CSS_SELECTOR, value='.jobs-save-button')
        save_button.click()

        # execute script to scroll to the bottom of the an element
        driver.execute_script(script="const targetElement = document.querySelector('.jobs-search__job-details--container');targetElement.scrollTop = targetElement.scrollHeight;")
        time.sleep(2)
        
        follow_button = driver.find_element(by=By.CSS_SELECTOR, value='.follow')
        if follow_button.text == 'Follow':
            follow_button.click()
        time.sleep(5)
        
    driver.close()

except NoSuchElementException as no_element_exception:
    print(no_element_exception)
    print('Element does not exist')
