import pandas as pd

def open_df(self, filepath):
    return pd.read_csv(filepath, sep=';', quotechar='"')