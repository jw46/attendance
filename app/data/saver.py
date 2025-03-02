import pandas as pd

def save_df(df, filepath):
    return df.to_csv(filepath, sep=';', quotechar='"')