import pandas as pd

def open_df(filepath):
    return pd.read_csv(filepath, sep=';', quotechar='"')