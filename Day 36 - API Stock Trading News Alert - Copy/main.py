from twilio.rest import Client
import requests


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# From Alpha Vantage, in order to have access to Stock Information.
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "*****************"

# From NEWS Api
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "*****************"

# From Twilio
account_sid = "*****************"
auth_token = "*****************"


# When STOCK price increase/decreases by 10% between yesterday and the day before yesterday then print("Get News").
stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]


# Yesterday
yesterday_data = data_list[0]
yesterday_data_open = yesterday_data['1. open']
yesterday_data_close = yesterday_data['4. close']
print(yesterday_data_close)


# Day Before Yesterday
bef_yesterday_data = data_list[1]
bef_yesterday_data_open = bef_yesterday_data['1. open']
bef_yesterday_data_close = bef_yesterday_data['4. close']
print(bef_yesterday_data_close)


# Positive Difference between Yesterday's and Day's Before Closing Price
diff = float(yesterday_data_close) - float(bef_yesterday_data_close)
up_or_down = None
if diff < 0:
    up_or_down = "🔻"
else:
    up_or_down = "🔺"

diff_percent = round((diff/ float(yesterday_data_close)) * 100)
print(f"Difference Percentage: {diff_percent}%")


# Get the first 3 news pieces for the COMPANY_NAME.

news_params = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME,
}

if abs(diff_percent) >= 10:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    # First Three Articles related to the Company_Name
    three_articles = articles[:3]
    print(three_articles)


# Create new List for the Three Articles Headline and Description
formatted_articles_list = [f"{STOCK}: {up_or_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
client = Client(account_sid, auth_token)
for article in formatted_articles_list:
    message = client.messages \
        .create(
        body=article,
        from_="*****************",
        to="*****************",
    )
print(message.status)
