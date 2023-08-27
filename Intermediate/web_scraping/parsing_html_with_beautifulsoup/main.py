from bs4 import BeautifulSoup
import requests

# SCRAPING A LIVE WEBSITE

response = requests.get(url='https://news.ycombinator.com/news')
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')

titles = soup.select(selector='.titleline a')
score_text = soup.select(selector='.score')

title_texts = [title.getText() for title in titles]
title_links = [title.get('href') for title in titles]
score_nos = [int(score.getText()[0:2]) for score in score_text]

# print(title_texts)
# print(title_links)
# print(score_nos)

# get max score from the list of scores
max_score = max(score_nos)
# get the max score index which will them be used to get the corresponding article title and link
max_score_index = score_nos.index(max_score)

# get the title, link, and score for the highest score
highest_score_title = title_texts[max_score_index]
highest_score_link = title_links[max_score_index]

print(f"Title: {highest_score_title}\nLink: {highest_score_link}\nScore: {max_score}")



# --------------------------------------------------------------------------------------- #
# --------------------------------------------------------------------------------------- #
# --------------------------------------------------------------------------------------- #
# --------------------------------------------------------------------------------------- #

# SCRAPING STATIC DATA

# import lxml

# # open the webite file
# with open('website.html') as file:
#     contents = file.read()

# # using lxml parser
# # soup = BeautifulSoup(contents, 'lxml')

# soup = BeautifulSoup(contents, 'html.parser')

# # get the title tag (the fitst title tag alone)
# # print(soup.title)

# # get the name of the title tag
# # print(soup.title.name)

# # get string that is within the title tag
# # print(soup.title.string)

# # get entire html
# # print(soup)

# # get the first a tag alone from the html 
# # print(soup.a)

# # get all a tags or all of aother elements
# all_a_tags = soup.find_all(name='a')

# # getting just the text within the a tags
# for tag in all_a_tags:
#     # print(tag.string)
#     # print(tag.getText())
    
#     # get attribute value
#     print(tag.get('href'))

# # get only the first element with h1 tag and an id of name
# heading = soup.find(name='h1', id='name')
# print(heading)

# section_heading = soup.find(name='h3', class_='heading')
# print(section_heading)

# # css selectors can be used to select specific elemnets
# company_url = soup.select_one(selector='p a')
# print(company_url)

# print(soup.select(selector='.heading'))