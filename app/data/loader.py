import pandas as pd

def open_df(filepath):
    return pd.read_csv(filepath, dtype=str, sep=';', quotechar='"', keep_default_na=False)