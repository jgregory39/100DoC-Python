import requests
from datetime import datetime
import time
import smtplib

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude
MY_EMAIL = 'fake@gmail.com'
MY_PASSWORD = 'insecure22'


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5


# Your position is within +5 or -5 degrees of the ISS position.

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    return not sunrise <= time_now <= sunset


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    if is_iss_overhead() and is_night():
        print("LOOK UP")
        # Cannot send email because gmail api functionality has been altered to only allow secure programs
        # connection = smtplib.SMPT("smtp.gmail.com", port=587)
        # connection.starttls()
        # connection.login(MY_EMAIL, MY_PASSWORD)
        # connection.sendmail(
        #     from_addr=MY_EMAIL,
        #     to_addrs=MY_EMAIL,
        #     msg="Subject:Look Up\n\nThe ISS is above you in the sky."
        # )

    time.sleep(60)
