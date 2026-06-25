import yfinance as yf
from pathlib import Path

class StockExtractor():
    def __init__(self, tickers:  list[str], period:str):
        self.tickers = tickers
        self.period = period

    def download(self):
        dataFrame = {}
        for c in self.tickers:
            df_temp = yf.download(c, period=self.period)
            df_temp.columns = df_temp.columns.droplevel("Ticker")

            clean_ticker = self.clean_ticker_name(c)

            dataFrame[clean_ticker] = df_temp

        self.data = dataFrame

        folder = Path(__file__).resolve().parent.parent.parent / "data" / "raw"
        print(folder)
        folder.mkdir(parents=True, exist_ok=True)        

        for ticker, df in self.data.items():
             file = folder / f"{ticker}.xlsx"
             df.to_excel(file)
    

        return dataFrame
    
    def clean_ticker_name(self, ticker):
            return ticker.replace("^", "")
