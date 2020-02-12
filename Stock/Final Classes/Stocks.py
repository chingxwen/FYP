#installations
#!pip install yfinance
#!pip install CurrencyConverter

#imports
from currency_converter import CurrencyConverter
import pandas as pd
import numpy as np
from datetime import date
import yfinance as yf


class StockData:
    
    def __init__(self, fromdate, todate, stock):
        self.fromdate = fromdate
        self.todate= todate
        self.stock = stock
        
    
    #yfinance scraper
    def yfinance_scraper(self):
        
        Data = yf.download(self.stock, start = self.fromdate, end = self.todate)
        Data.to_csv(self.stock + ".csv")
    
        return Data
    
    #cleanse
    def cleanse_stock(self):

        # Read freshly downloaded file
        data = pd.read_csv(self.stock + ".csv")
        #data = Data

        # Remove rows with null values
        data['High'] = data['High'].replace('null', np.nan)
        dg = data.dropna(axis=0, subset=['High'])
        #renaming columns
        dg.rename(columns={'Adj Close':'adj_close', 'Date':'date',
                             'Volume': 'volume', 'Close':'close', 'High': 'high', 
                             'Low': 'low', 'Open':'open'}, inplace = True)

        # Change data to a dataframe
        df = pd.DataFrame(dg)
        #print(df)

        Stockname = []

        for i in range (len(df.high)):
            Stockname.append(self.stock)

        # Add a column and column name
        df.insert(7, "Stockname", Stockname , True)
        #print(df)

        return df
    
    #prepare
    def prepare_stock(self,df):

        # read file
        data = df

        #convert  date data to datetime format
        theDates =  pd.to_datetime(data['date'], format='%Y/%m/%d')

        #convert KRW to USD
        c = CurrencyConverter('http://www.ecb.int/stats/eurofxref/eurofxref-hist.zip', fallback_on_missing_rate=True)
        def convert(amount, dateyear, datemonth, dateday):
        #     value = amount
            value = c.convert(amount, input("Please input the foreign currency: "), "USD", date=date(dateyear, datemonth, dateday))

            return value

        convertopenarrStart = []
        converthigharrStart = []
        convertlowarrStart = []
        convertclosearrStart = []
        convertadjclosearrStart = []
        ndates = []
        nopen = []
        nhigh = []
        nlow = []
        nclose = []
        nadj_close = []
        nvolume = []
        nstockname = []
        ndf = pd.DataFrame()

        for i in range(len(data.open)):
            ndates.append(theDates[i])
            nopen.append(data.open[i])
            nhigh.append(data.high[i])
            nlow.append(data.low[i])
            nclose.append(data.close[i])
            nadj_close.append(data.adj_close[i])
            nvolume.append(data.volume[i])
            nstockname.append(data.Stockname[i])
            convertopen1 = float(convert(data.open[i], theDates[i].year, theDates[i].month, theDates[i].day))
            convertopenarrStart.append(convertopen1)
            converthigh1 = float(convert(data.high[i], theDates[i].year, theDates[i].month, theDates[i].day))
            converthigharrStart.append(converthigh1)
            convertlow1 = float(convert(data.low[i], theDates[i].year, theDates[i].month, theDates[i].day))
            convertlowarrStart.append(convertlow1)
            convertclose1 = float(convert(data.close[i], theDates[i].year, theDates[i].month, theDates[i].day))
            convertclosearrStart.append(convertclose1)
            convertadjclose1 = float(convert(data.adj_close[i], theDates[i].year, theDates[i].month, theDates[i].day))
            convertadjclosearrStart.append(convertadjclose1)

        ndf.insert(0, 'date', ndates, True)
        ndf.insert(1, 'open', nopen, True)
        ndf.insert(2, 'high', nhigh, True)
        ndf.insert(3, 'low', nlow, True)
        ndf.insert(4, 'close', nclose, True)
        ndf.insert(5, 'adj_close', nadj_close, True)
        ndf.insert(6, 'volume', nvolume, True)
        ndf.insert(7, 'Stockname', nstockname, True)
        ndf.insert(8, 'Open_USD', convertopenarrStart, True)
        ndf.insert(9, 'High_USD', converthigharrStart, True)
        ndf.insert(10, 'Low_USD', convertlowarrStart, True)
        ndf.insert(11, 'Close_USD', convertclosearrStart, True)
        ndf.insert(12, 'Adj_Close_USD', convertadjclosearrStart, True)

        pd.DataFrame.from_dict(data=ndf, orient='columns').to_csv(self.fromdate + "." + self.todate + "." + self.stock + ".csv")

        return ndf