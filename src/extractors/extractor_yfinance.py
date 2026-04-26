import yfinance as yf

class StockExtractor():
    def __init__(self, tickers:  list[str], period:str):
        self.tickers = tickers
        self.period = period

    def download(self):
        self.data = yf.download(self.tickers, period=self.period)
        
        return self.data