# Please make sure that the library has already been downloaded
# pip install yfinance
import yfinance as yf

fromdate = input("Please input the start date to be extracted(yyyy-mm-dd): ")
todate = input("Please input the start date to be extracted(yyyy-mm-dd): ")
stock = input("Please input which stock you would like to extract in its index format: ")

data = yf.download(stock, start = fromdate, end = todate)
data.to_csv(stock + ".csv")