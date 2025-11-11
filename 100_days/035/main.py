import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

parameters = {
    "lat": "44.786568",
    "lon": "20.448921",
    "units": "metric",
    "cnt": 4,
    "appid": os.getenv("API_KEY")
}

URL = "http://api.openweathermap.org/data/2.5/forecast"
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

def get_weather_data(i):

    try:
        response = requests.get(URL, params=parameters)
        response_json = response.json()
        return response_json['list'][i]['weather'][0]['id']

    except requests.exceptions.HTTPError as err:
        print(err)
        return []

condition_code = []
will_rain = False

for i in range(4):
    condition_code.append(get_weather_data(i))

for n in range(len(condition_code)):
    if condition_code[n] < 800:
        will_rain = True

if will_rain:
    message = client.messages.create(
        body="It will rain in the next 12 hours! Bring an umbrella!",
        from_="+14199484604",
        to="+381643691466",
    )

