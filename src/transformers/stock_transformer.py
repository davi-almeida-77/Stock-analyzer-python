import pandas as pd

class StockTransformer():
    def __init__(self, data):
        self.data = data

    def transform(self):
        df = self.data.stack(level="Ticker")

        return df