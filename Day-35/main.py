import requests
from dotenv import load_dotenv
import os
from twilio.rest import Client

# Open Weather API
load_dotenv()
API_KEY = os.environ.get('OWM_API_KEY')
LAT = '37.43'
LON = '78.656'


# Twillio API
TWILLIO_PHONE_NUMBER = '+16802195070'
RECEIVING_PHONE_NUMBER = '+18452745432'
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")

# Check if it will rain
response = requests.get(url=f"http://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&appid={API_KEY}&cnt=4")
weather_list = response.json()['list']

forcast = ''
will_rain = False
for event in weather_list:
    weather = event['weather'][0]
    if weather['main'] == 'Clouds':
        forcast = f"At approximately {event['dt_txt']} there will be {weather['description']}."
        will_rain = True

# Send Sms
if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body=forcast,
        from_=MY_PHONE_NUMBER,
        to=RECEIVING_PHONE_NUMBER
    )
    print(message.status)