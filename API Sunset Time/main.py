import requests
from datetime import datetime

# Sweden - Gothenburg
MY_LAT = 57.696991
MY_LNG = 11.986500

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)

sunrise = data["results"]["sunrise"].split("T")[1]
sunset = data["results"]["sunset"].split("T")[1]

sun = (sunrise, sunset)
print(f"Sunrise: {sun[0]}")
print(f"Sunset: {sun[1]}")

time_now = datetime.now()
print(f"Current Time: {time_now.hour}:{time_now.minute}:{time_now.second}")