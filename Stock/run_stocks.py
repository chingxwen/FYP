# required installations 
# pip install yfinance
# pip install CurrencyConverter

import Stocks

stocks_extract = Stocks.StockData(input("Please input the start date to be extracted(yyyy-mm-dd): "),
                  input("Please input the end date to be extracted(yyyy-mm-dd): "),
                  input("Please input which stock you would like to extract in its index format: "))
ExtractData = stocks_extract.yfinance_scraper()
CleansedData = stocks_extract.cleanse_stock()
PreparedData = stocks_extract.prepare_stock(CleansedData)
