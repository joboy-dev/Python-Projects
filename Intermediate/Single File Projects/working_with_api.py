import requests

response = requests.get(url='http://api.open-notify.org/iss-now.json')

# raise exception if status code is not 200
response.raise_for_status()

# getting the json data
data = response.json()
print(data)

longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']

iss_position = (longitude, latitude)
print(iss_position)