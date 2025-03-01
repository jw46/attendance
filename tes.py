import pandas as pd

df = pd.read_csv('/home/jon/temp/df.csv', dtype=str, sep=';', quotechar='"')
# print(df)

columns = df.columns

def get_pritty_row(row):
    return list(map(lambda x: row[x], columns))

# for index, row in df.iterrows():
#     print(get_pritty_row(row))

max_lengths = list(map(lambda x: int(df[x].str.len().max()), columns))
print(max_lengths)