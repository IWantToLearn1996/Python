import requests
from twilio.rest import Client

# It requires OpenWeather subscription for the OneCall
OWN_Endpoint = "**************************************"
api_key = "**************************************"

# From LatLong.Net
LAT = 57.696991
LON = 11.986500

# It requires Twilio subscription to send a Message
account_sid = "**************************************"
auth_token = "**************************************"

weather_parameters = {
    "lat": LAT,
    "lon": LON,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response = requests.get(OWN_Endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()

clear_sky = False
will_rain = False
will_snow = False

for hour in range(0, 12):
    condition_code = weather_data["hourly"][hour]["weather"][0]["id"]
    if int(condition_code) < 600:
        will_rain = True
    elif int(condition_code) >= 600 and int(condition_code) < 700:
        will_snow = True
    elif int(condition_code) >= 800:
        clear_sky = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="Hey... It's going to RAIN Cats and Dogs today... Take an Umbrella!",
            from_="************",
            to="************"
    )
    print(message.status)
elif will_snow:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="Hey... It's going to SNOW today... Put on warm clothes!",
            from_="************",
            to="************"
    )
    print(message.status)
elif clear_sky:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="Hey... GUESS WHAT... Take your Sunglasses!",
            from_="************",
            to="************"
    )
    print(message.status)

# For Daily Messages in a specific hour -> Python Anywhere by Anaconda
