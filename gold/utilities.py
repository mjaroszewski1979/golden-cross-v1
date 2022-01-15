import pandas_datareader as pdr
import pandas as pd
from pandas_datareader._utils import RemoteDataError
import datetime
import talib



end_d = datetime.datetime.now()
diff = datetime.timedelta(days = 600)
start_d = end_d - diff

def get_trend_data(start=start_d, end=end_d, symbol='BTC-USD'):
    items = {}
    try:
        data = pdr.get_data_yahoo(symbol, start, end)
        items['close'] = data['Adj Close']
        items['last_close'] = data['Adj Close'][-1]
        items['error'] = None
    except RemoteDataError:
        items['error'] = 'Fetching data failed due to an error on the yahoo finance server. Please come back later.'
        
    return items

data = get_trend_data()

# Creating indicators class which inherits from YahooData
class Indis:
    def __init__(self):
        self.last_close = data['last_close']
        self.close = data['close']
        self.error = data['error']
        self.period = 252
        
        # Using Technical Analysis Library to create an extensive list of trading indicators
        self.dema = talib.DEMA(self.close, self.period)
        self.ema = talib.EMA(self.close, self.period)
        self.ht = talib.HT_TRENDLINE(self.close)
        self.kama = talib.KAMA(self.close, self.period)
        self.mama, self.fama = talib.MAMA(self.close, fastlimit=0.5, slowlimit=0.05)
        self.sma = talib.SMA(self.close, self.period)
        self.t3 = talib.T3(self.close, self.period, vfactor=0.7)
        self.wma = talib.WMA(self.close, self.period)
        self.trima = talib.TRIMA(self.close, self.period)

        self.scores = [self.dema, self.ema, self.ht, self.kama, self.fama, 
               self.sma, self.t3, self.trima, self.wma]

        # List of indicators last readings
        self.results = [ score[-1] for score in self.scores ]
        
        self.values = [ self.last_close for _ in range(len(self.results)) ]

        # List of indicators names
        self.names = ['Double Exponential Moving Average', 'Exponential Moving Average','Hilbert Transform - Instantaneous Trendline', 'Kaufman Adaptive Moving Average',
            'MESA Adaptive Moving Average', 'Simple Moving Average', 'Triple Exponential Moving Average', 'Triangular Moving Average', 'Weighted Moving Average']

indis = Indis()

