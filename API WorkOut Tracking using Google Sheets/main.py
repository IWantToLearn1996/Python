from datetime import datetime
import requests

# Nutritionix Api Account
APPLICATION_ID = "*****************"
NUTRITION_API_KEY = "*****************"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# From mattsilv GitHub Profile: https://gist.github.com/mattsilv/d99cd145cc2d44d71fa5d15dd4829e03
headers = {
    "x-app-id": APPLICATION_ID,
    "x-app-key": NUTRITION_API_KEY,
}

parameters = {
    "query":"exercise_text",
    "gender":"male",
    "weight_kg":85,
    "height_cm":185,
    "age":30
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

sheet_endpoint = "https://docs.google.com/spreadsheets/d/1FBITn68CY5zjldme86BUZh1GkJAIUlw7DM5sTvd7kcQ/edit#gid=0"

today = datetime.now().strftime("%d%m%Y")
time_now = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_input = {
        "workout": {
            "date": today,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

sheet_response = requests.post(sheet_endpoint, json=sheet_input)
print(sheet_response.text)

# Basic Authentication
sheet_response = requests.post(
    sheet_endpoint,
    json=sheet_inputs,
    auth=(
        "****************",
        "****************",
    )
)

# Bearer Token Authentication
bearer_headers = {
    "Authorization": "*****************"
}
sheet_response = requests.post(
    sheet_endpoint,
    json=sheet_input,
    headers=bearer_headers
)