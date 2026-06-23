import yfinance as yf

class StockExtractor():
    def __init__(self, tickers:  list[str], period:str):
        self.tickers = tickers
        self.period = period

    def download(self):
        dataFrame = {}
        for c in self.tickers:
            df_temp = yf.download(c, period=self.period)
            df_temp.columns = df_temp.columns.droplevel("Ticker")
            dataFrame[c] = df_temp

        self.data = dataFrame

        return dataFrame
    
