from configparser import ConfigParser
import requests
from datetime import datetime
import json

config = ConfigParser()
config.read('config.ini')

# use NUTRITIONIX to parse exercise
NUTRITIONIX_APP_ID = config['NUTRITIONIX']['APP_ID']
NUTRITIONIX_API_KEY = config['NUTRITIONIX']['API_KEY']

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_headers = {
    'x-app-id': NUTRITIONIX_APP_ID,
    'x-app-key': NUTRITIONIX_API_KEY
}

query = input("Tell me what exercises you did:")

nutritionix_params = {'query': query}

response = requests.post(url=nutritionix_endpoint, data=nutritionix_params, headers=nutritionix_headers)
exercise = response.json()['exercises'][0]

duration = exercise['duration_min']
calories = exercise['nf_calories']
activity = exercise['name'].title()

# use SHEETY to update spreadsheet
SHEETY_KEY = config['SHEETY']['BEARER_TOKEN']
SHEETY_ENDPOINT = config['SHEETY']['ENDPOINT']

sheety_headers = {
    'Authorization': f"Bearer {SHEETY_KEY}",
    'Content-Type': 'application/json'
}

today = datetime.now()

sheety_body = json.dumps({
    "workout": {
        "date": today.strftime('%m/%d/%Y'),
        "time": today.strftime('%H:%M:%S'),
        "exercise": activity,
        "duration": duration,
        "calories": calories
    }
})

response = requests.post(url=SHEETY_ENDPOINT, data=sheety_body, headers=sheety_headers)
print(response.status_code)