import yfinance as yf

def StockDownloader():
    """ 
    Please make sure that the library has already been downloaded: pip install yfinance
    The dates entered have to be in the yyyy-mm-dd format
    Stock indexs have to be in capitalised alphabet
    """
    fromdate = input("Please input the start date to be extracted(yyyy-mm-dd): ")
    todate = input("Please input the start date to be extracted(yyyy-mm-dd): ")
    stock = input("Please input which stock you would like to extract in its index format: ").upper()

    data = yf.download(stock, start = fromdate, end = todate)
    data.to_csv(stock + ".csv")
    return stock 
StockDownloader()