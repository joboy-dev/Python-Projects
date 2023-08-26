import requests
from datetime import datetime

USERNAME = 'josephkorede36'
TOKEN = 'hgj5rjdnsk3fk95kdclg44gh'
GRAPH_ID = 'codegraph1'

pixela_endpoint = 'https://pixe.la/v1/users'

# -------------- CREATING POST REQUEST ------------- #

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    'id': 'codegraph1',
    'name': 'Coding Habit Graph',
    'unit': 'Hour',
    'type': 'float',
    'color': 'shibafu'
}

graph_headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=graph_headers)
# print(response.text)

pixel_creation_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

today = datetime.now().date()
today_date_formatted = today.strftime("%Y%m%d")
print(today_date_formatted)

pixel_data = {
    'date': today_date_formatted,
    'quantity': '10.1'
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=graph_headers)
print(response.text)

# Using PUT is similar to using POST. Just read documentation of the API you want to work on to know how to utilize their endpoint

# Usind DELETE requures an endpoint and headers only, no need for json