import pandas as pd

class StockTransformer():
    def __init__(self, data):
        self.data = data

    def transform(self):
        df = pd.concat(objs=self.data.values(), keys=self.data.keys())

        return df