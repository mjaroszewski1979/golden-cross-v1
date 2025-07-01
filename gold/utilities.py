from datetime import timedelta
import requests
import numpy as np
import talib

# Mailchimp imports
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

# Django imports
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.utils import timezone

# App imports
from .models import Bitcoin


def get_data():
    """
    Fetch and process Bitcoin data from Yahoo Finance.
    Calculates various technical indicators and updates the Bitcoin model instance.
    """
    
    # Get the Bitcoin object or create it if it doesn't exist
    btc, created = Bitcoin.objects.get_or_create(title='btc-usd')

    # Check if the data is fresh (less than 24 hours old)
    if not created and timezone.now() - btc.date_added < timedelta(hours=24):
        print("✔ Data loaded from cache (not older than 24h)")
        return  # or return the data if needed

    # Fetch current price data from CoinGecko
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
    headers = {
        'x-cg-pro-api-key': 'CG-jL5hH7oCAaSMYSywH3oV6bxA'
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Fetching error:", response.status_code, response.text)
        return

    data = response.json()
    try:
        price = data['bitcoin']['usd']
    except KeyError:
        print("Invalid response format:", data)
        return

    # Calculate technical indicators using the current price repeated over the period
    period = 252
    close = np.array([price] * period, dtype='float64')
    high = np.array([price] * period, dtype='float64')
    low = np.array([price] * period, dtype='float64')

    results = [
        talib.DEMA(close, period)[-1],
        talib.EMA(close, period)[-1],
        talib.HT_TRENDLINE(close)[-1],
        talib.KAMA(close, period)[-1],
        talib.SAR(high, low, acceleration=0.020, maximum=0.2)[-1],
        talib.SMA(close, period)[-1],
        talib.TRIMA(close, period)[-1],
        talib.WMA(close, period)[-1],
    ]

    # Determine signal: 'buy' if indicator <= price, otherwise 'sell'
    fields = ['sell' if r > price else 'buy' for r in results]

    # Save signals and the current timestamp to the database
    btc.dema = fields[0]
    btc.ema = fields[1]
    btc.ht = fields[2]
    btc.kama = fields[3]
    btc.sar = fields[4]
    btc.sma = fields[5]
    btc.trima = fields[6]
    btc.wma = fields[7]
    btc.date_added = timezone.now()
    btc.save()
    print("Data fetched and saved")

# Mailchimp configuration settings
api_key = settings.MAILCHIMP_API_KEY
server = settings.MAILCHIMP_DATA_CENTER
list_id = settings.MAILCHIMP_EMAIL_LIST_ID

def subscribe(email):
    """
    Subscribe a user to the Mailchimp email list.
    
    Args:
        email (str): The email address to be subscribed.
    """

    # Initialize the Mailchimp client with API key and server information
    client = MailchimpMarketing.Client()
    client.set_config({
        "api_key": api_key,
        "server": server,
    })

    # Define the member information for the subscription
    member_info = {
        "email_address": email,
        "status": "subscribed",
    }

    try:
        # Attempt to add the email to the Mailchimp list
        response = client.lists.add_list_member(list_id, member_info)
        print("response: {}".format(response))
        
    except ApiClientError as error:
        # Handle any API client errors
        print("An exception occurred: {}".format(error.text))


    









