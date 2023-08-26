import requests
import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(os.path.join(BASE_DIR, ".env"))

# --------------- USING DATETIME MODULE ------------------ #
today = datetime.now().date().strftime('%d/%m/%Y')
# print(today)
time = datetime.now().time().strftime('%H:%M:%S')
# print(time)

#------------------ NUTRITIONIX API ---------------------- #

NUTRITIONIX_APP_ID = os.getenv('NUTRITIONIX_APP_ID')
NUTRITIONIX_API_KEY = os.getenv('NUTRITIONIX_API_KEY')

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'


query = input('Tell me which exercises you did: ')

exercise_headers = {
    'x-app-id': NUTRITIONIX_APP_ID,
    'x-app-key': NUTRITIONIX_API_KEY,
    'Content-Type': 'application/json'
}

exercise_data = {
    'query': query,
    'gender': 'nale',
    'weight_kg': 55,
    'height_cm': 172,
    'age': 19
}

exercise_response = requests.post(url=exercise_endpoint, headers=exercise_headers, json=exercise_data)

exercise_output = exercise_response.json()

exercises = exercise_output['exercises']

#------------------------ SHEETY API ------------------------ #

SHEETY_AUTH_TOKEN = os.getenv('SHEETY_AUTH_TOKEN')

sheety_endpoint = 'https://api.sheety.co/88896027d59dd2ab37182eea7de0e12f/myWorkouts/workouts'

sheety_headers = {
    'Authorization': f'Bearer {SHEETY_AUTH_TOKEN}'
}

for exercise in exercises:
    sheety_data = {
        'workout': {
            'date': today,
            'time': time,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories'],
            'id': exercise['tag_id']
        }
        
    }

    sheety_response = requests.post(url=sheety_endpoint, headers=sheety_headers, json=sheety_data)

sheety_output = sheety_response.json()
print(sheety_output)
