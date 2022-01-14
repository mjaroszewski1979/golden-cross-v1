import pandas_datareader as pdr
import pandas as pd
from pandas_datareader._utils import RemoteDataError
import datetime


def get_data(symbols):
    end_d = datetime.datetime.now()
    diff = datetime.timedelta(days = 252)
    start_d = end_d - diff
    results = []
    for symbol in symbols:
        try:
            data = pdr.get_data_yahoo(symbol, start=start_d, end=end_d) 
            ma200 = data['Adj Close'].pct_change(periods=200) * 100 
            ma50 = data['Adj Close'].pct_change(periods=50) * 100 
            if ma50[-2] < ma200[-2] and round(ma50[-1], 2) == round(ma200[-1], 2):
                results.append('golden cross')
            else:
                results.append('no cross')
        except RemoteDataError:
            results.append('YF error')
    return results

stocks = ['^GSPC', '^IXIC', '^DJI']
data = get_data(stocks)
results = {}
for x in data:

    results = {
        'spx' : x[-1],
        'ndx': x[-2],
        'dji': x[-3]
    }