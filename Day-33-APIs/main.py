import requests
from datetime import datetime

# Get ISS current location
response = requests.get(url='http://api.open-notify.org/iss-now.json')
response.raise_for_status()

data = response.json()["iss_position"]

iss_long = data['longitude']
iss_lat = data['latitude']

parameters = {
    'lat': iss_lat,
    'long': iss_long,
    'formatted': 0
}
response = requests.get(url=f"https://api.sunrise-sunset.org/json?lat={iss_lat}&lng={iss_long}&formatted=0")
response.raise_for_status()

data = response.json()
sunrise = data['results']['sunrise'].split("T")[1].split(':')[0]
sunset = data['results']['sunset'].split("T")[1].split(':')[0]
print(sunrise)
print(sunset)

time_now = datetime.now().hour
print(time_now)