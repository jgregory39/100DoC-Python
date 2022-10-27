import requests
from configparser import ConfigParser
from html import unescape
import os
from twilio.rest import Client
from datetime import date, timedelta
from newsapi import NewsApiClient

STOCK = "TSLA"
COMPANY_NAME = "Tesla"


config = ConfigParser()
config.read('.project_config')
alpha_vantage_key = config['API']['ALPHA_VANTAGE_KEY']
news_api_key = config['API']['NEWS_API_KEY']
twilio_account_ssid = config['API']['TWILIO_ACCOUNT_SID']
twilio_auth_token = config['API']['TWILIO_AUTH_TOKEN']
twilio_phone_number = config['API']['TWILIO_PHONE_NUMBER']
receiving_phone_number = config['API']['RECEIVING_PHONE_NUMBER']


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def get_stocks():
    stock_url = 'https://www.alphavantage.co/query'
    stock_params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': STOCK,
        'interval': '60min',
        'apikey': alpha_vantage_key
    }
    response = requests.get(url=stock_url, params=stock_params)
    yesterday = date.today() - timedelta(days=1)
    day_before = yesterday - timedelta(days=1)

    yesterday_close = float(response.json()['Time Series (60min)'][f'{yesterday} 16:00:00']['4. close'])
    day_before_close = float(response.json()['Time Series (60min)'][f'{day_before} 16:00:00']['4. close'])

    delta_close = yesterday_close - day_before_close

    return delta_close / yesterday_close


# STEP 2: Use https://newsapi.org

def get_news():
    newsapi = NewsApiClient(api_key=news_api_key)
    top_headlines = newsapi.get_top_headlines(q=COMPANY_NAME)
    articles = [{'title': unescape(article['title']), 'description': unescape(article['description'])}
                for article in top_headlines['articles'][:3]]
    return articles


# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
def send_alert(delta, articles):
    delta_perc = round(delta * 100)
    report = f"{STOCK}: {'🔺' if delta > 0 else '🔻'}{delta_perc}%\n"
    for article in articles:
        report += f"Headline: {article['title']}\n"
        report += f"Brief: {article['description']}\n"

    client = Client(twilio_account_ssid, twilio_auth_token)
    sms_message = client.messages.create(
        body=report,
        from_=twilio_phone_number,
        to=receiving_phone_number
    )
    print(sms_message.status)


delta_stocks = get_stocks()
if abs(delta_stocks > 0.05):
    news = get_news()
    send_alert(delta_stocks, news)


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
