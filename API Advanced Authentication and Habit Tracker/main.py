import requests
from datetime import datetime


# Create a PIXELA Account with your OWN Username and Token
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "iwanttolearn1996"
TOKEN = "*****************"
GRAPH_ID = "*****************"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Hours",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# yesterday = datetime(year=2023, month=3, day=12)
today = datetime.now()

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many HOURS have you coded today? "),
}

response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)

update_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"

update_params = {
    "quantity": "3",
}

# response = requests.put(url=update_endpoint, json=update_params, headers=headers)
# print(response.text)

# delete_endpoint = f"{update_endpoint}"
#
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
