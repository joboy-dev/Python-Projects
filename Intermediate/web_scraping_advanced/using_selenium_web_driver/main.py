from selenium import webdriver
from selenium.webdriver.common.by import By  # for finding elements

# chrome_driver_path = "C:/Development/chromedriver.exe"
# driver = webdriver.Chrome()

# # open up a webpage
# driver.get('https://www.amazon.com/SAMSUNG-Smartphone-Unlocked-Brightest-Processor/dp/B09MVZ93YN/ref=sr_1_2_sspa?keywords=samsung%2Bgalaxy%2Bs21&qid=1693258405&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1')

# # finding and selecting html elements to act on
# price = driver.find_element(by=By.CSS_SELECTOR, value='.a-price .a-offscreen')
# print(price.text)


# # close the driver
# driver.close()


# driver.find_elements(by=By.CSS_SELECTOR, value='.a-price .a-offscreen')

# How an xpath looks like
# //*[@id="classifiers"]/div[10]/button


# CHALLENGE
driver = webdriver.Chrome()

driver.get('https://www.python.org/')

event_names = driver.find_elements(by=By.CSS_SELECTOR, value='.event-widget ul li a')

event_dates = driver.find_elements(by=By.CSS_SELECTOR, value='.event-widget ul li time')

event_names_list = [name.text for name in event_names]
print(event_names_list)

event_dates_list = [date.get_attribute('datetime')[0:10] for date in event_dates]
print(event_dates_list)

events_dict = {
    index: {'time': event_dates_list[index], 'name': event_names_list[index]} for index in range(len(event_names_list))
}
print(events_dict)

driver.close()