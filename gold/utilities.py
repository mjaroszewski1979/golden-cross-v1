import pandas_datareader as pdr
import pandas as pd
from pandas_datareader._utils import RemoteDataError
import datetime
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

    # Define the time period for the data
    end_d = datetime.datetime.now()
    diff = datetime.timedelta(days = 600)
    start_d = end_d - diff
    period = 252
    
    try:
        # Fetch the Bitcoin data from Yahoo Finance
        data = pdr.get_data_yahoo('BTC-USD', start=start_d, end=end_d)

        # Extract relevant data columns
        close = data['Adj Close']
        high = data['High']
        low = data['Low']
        last_close = data['Adj Close'][-1]

        # Calculate various technical indicators using TA-Lib
        results = [
            talib.DEMA(close, period)[-1], 
            talib.EMA(close, period)[-1],
            talib.HT_TRENDLINE(close)[-1],
            talib.KAMA(close, period)[-1],
            talib.SAR(high, low, acceleration=0.020, maximum=0.2)[-1],
            talib.SMA(close, period)[-1],
            talib.TRIMA(close, period)[-1],
            talib.WMA(close, period)[-1]
            ]

        # Determine whether to 'buy' or 'sell' based on the indicator values
        fields = []
        for result in results:
            if result > last_close:
                fields.append('sell')
            else:
                fields.append('buy')

        # Fetch the Bitcoin model instance and update its fields
        btc = get_object_or_404(Bitcoin, title='btc-usd')
        btc.dema = fields[0]
        btc.ema = fields[1]
        btc.ht = fields[2]
        btc.kama = fields[3]
        btc.sar = fields[4]
        btc.sma = fields[5]
        btc.trima = fields[6]
        btc.wma = fields[7]
        btc.date_added = datetime.datetime.now(tz=timezone.utc)
        btc.save()
        
    except RemoteDataError:
        # Handle any errors that occur during data fetching
        print('connection error')

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


    









