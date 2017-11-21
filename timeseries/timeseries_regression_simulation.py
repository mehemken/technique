import pandas as pd
import numpy as np
import datetime


class data_generator:
    def __init__(self, n=100):
        self.n = 100
        self.df = pd.DataFrame()
        self.zips = self.zip_sample()
        self.dates = self.timestamp_sample()

    def get_sample(self):
        df = self.df

        df['Zip'] = self.zip_sample()
        df['Date'] = self.timestamp_sample()
        df['Amount'] = self.dollar_sample()

        return df

    def zip_sample(self, n=None):
        if not n:
            n = self.n

        zips = np.random.randint(90024, 90030, n)

        return pd.Series(zips)

    def days_offset_sample(self, n=None):
        if not n:
            n = self.n

        days_offset = np.floor(np.sqrt(np.random.normal(0, 20, n)**2))

        return pd.Series(days_offset)

    def timestamp_sample(self):
        def from_offset(x):
            t = datetime.timedelta(days=x)
            return datetime.date.today() - t
        offsets = self.days_offset_sample()
        return pd.Series(offsets).apply(from_offset)

    def dollar_sample(self, n=None):
        if not n:
            n = self.n

        y = np.random.randint(10, 900, n)

        return pd.Series(np.floor(y))
