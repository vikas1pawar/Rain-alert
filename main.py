import requests
import os
from twilio.rest import Client

OneCall = "https://api.openweathermap.org/data/2.5/onecall"
appKey = "10f9129e1229cbcfcdbc77a8b0a01b0b"
account_sid = "ACea8ff32ddad8af78d591c1f29f41f60f"
auth_token = "e8149e7142b045a0a0e122deda2f6fd1"

parameters = {
    "lat": 60.257140,
    "lon": 6.565120,
    "appid": appKey,
    "exclude": "current,minutely,daily"
}
response = requests.get(OneCall, params=parameters)
response.raise_for_status()
data = response.json()

weather_slice = data["hourly"][:12]
will_rain = False
for hour_data in weather_slice:
    ids = hour_data["weather"][0]["id"]
    if ids < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Hey! There raining outside, Take Umbrella outside.",
        from_="+17752566615",
        to="+917385699074"
    )
    print(message.status)

