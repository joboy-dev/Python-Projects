import requests
from bs4 import BeautifulSoup

# make request to the site
response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')
data = response.text

# initialize beautiful soup
soup = BeautifulSoup(data, 'html.parser')

# get all movie tags
movies = soup.find_all(name='h3', class_='listicleItem_listicle-item__title__hW_Kn')

# convert movie tags into text
movie_list = [movie.getText() for movie in movies]

# reverse the movie list
movie_list.reverse()
# print(movie_list)

# store what will be written to file in a variable
movies_text = '\n'.join(movie_list)
# print(movies_text)

# write to the movies.txt file
with open('movies.txt', 'w', encoding='utf-8') as movies_file:
    movies_file.write(f'Here are the top 100 greatest movies of all time\n{movies_text}')
