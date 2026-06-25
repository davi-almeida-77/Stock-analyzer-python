import pandas as pd

class StockTransformer():
    def __init__(self, data):
        self.data = data

    def transform(self):
        df = pd.concat(objs=self.data.values(), keys=self.data.keys())

        df["MM20"] = df.groupby(level=0)["Close"].transform(lambda x: x.rolling(20).mean())

        df["MM50"] = df.groupby(level=0)["Close"].transform(lambda x: x.rolling(50).mean())

        df["Diary_return"] = df.groupby(level=0)["Close"].transform(lambda x: x.pct_change())

        df["Volatility"] = df.groupby(level=0)["Diary_return"].transform(lambda x: x.rolling(20).std())


        return df