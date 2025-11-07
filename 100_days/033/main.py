import requests

URL = "http://api.open-notify.org/iss-now.json"
GET_SUNSET = "https://api.sunrise-sunset.org/json"

def get_iss_position():
    try:
        response = requests.get(URL)
        response.raise_for_status()
        data = response.json()
        lon = data['iss_position']["longitude"]
        lat = data['iss_position']["latitude"]
        iss_position = (lon, lat)
        print("ISS's now is here Longitude: ", iss_position)
        return iss_position
    except requests.exceptions.HTTPError as err:
        print(err)

def get_sunset(pos):
    try:
        response = requests.get(f"{GET_SUNSET}?lat={pos[0]}&lng={pos[1]}")
        response.raise_for_status()
        data = response.json()
        sunset = data['results']['sunset']
        print(f"Sunset is here at: {sunset} UTC")
        return sunset
    except requests.exceptions.HTTPError as err:
        print(err)

get_sunset(get_iss_position())
