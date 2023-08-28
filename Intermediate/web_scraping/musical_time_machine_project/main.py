import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path
from pprint import pprint

import spotipy
from spotipy import SpotifyException
from spotipy.oauth2 import SpotifyOAuth

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

# needed for oauth to spotify
SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')

# ----------------------------------------------------------- #
# ----------------------------------------------------------- #

def is_valid_date(date_string):
    '''Function to check if date format is valid'''
    try:
        # Attempt to parse the input date string using the specified format
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    
# ----------------------------------------------------------- #
# ----------------------------------------------------------- #

process = True
while process:
    user_input = input('Which year do you want to travel to. Type in this format: YYYY-MM-DD: ')
    year = int(user_input[0:4])
    # print(year)

    if not is_valid_date(user_input):
        print('Date is invalid. Try again.')
    else:
        try:
            response = requests.get(f'https://www.billboard.com/charts/hot-100/{user_input}')
            data = response.text
            process = False
        except Exception as e:
            print(f'ERROR: {e}\n\nConnect to the internet.')
            exit()
        
# ---------------- SONG LIST FROM BEAUTIFULSOUP ------------- #

soup = BeautifulSoup(data, 'html.parser')
song_tags = soup.select(selector='.lrv-a-unstyle-list li .c-title')

# get list of songs from the song tags text
song_list = [song.getText().strip() for song in song_tags]
print(song_list)

# ---------------- SPOTIFY AUTHENTICATION ------------------ #
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope='playlist-modify-private'  # to create a private playlist
))

# get currrent user data
current_user_data = sp.current_user()
# get user id
user_id = current_user_data['id']

# define new play list name
new_playlist_name = f'{user_input} Billboard 100'
print(f"A new playlist '{new_playlist_name}' will be created for you.")

# get a list of user playlists
user_playlists = sp.current_user_playlists()
all_user_playlists = user_playlists['items']
all_playlist_names = [playlist['name'] for playlist in all_user_playlists]
print(all_playlist_names)

# create playlist
playlist_data = sp.user_playlist_create(user=user_id, name=new_playlist_name, public=False)
# get playlist id
playlist_id = playlist_data['id']

# search for a song
for song in song_list:
    try:
        result = sp.search(f"track: {song} year: {year}")
        
        # get song url
        song_uris = result['tracks']['items'][0]['uri']
        
        # add song to created playlist
        sp.playlist_add_items(playlist_id=playlist_id, items=[song_uris])  # items has to be a list
        print(f'Song {song} added to playlist {new_playlist_name}')
    except SpotifyException as e:
        if e.http_status == 404:  # HTTP 404 indicates the track was not found
            print(f"Track {song} not available on Spotify.")
        else:
            print("An error occurred:", e)
    except Exception as ex:
        print('An error occured: ', ex)
        