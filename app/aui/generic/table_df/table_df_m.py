import pandas as pd

class TableDfModel:
    def __init__(self, source_filepath):
        self.source_filepath = source_filepath
        self.df = pd.read_csv(self.source_filepath, dtype=str, sep=';', quotechar='"')[['name']]
        self.columns = self.df.columns
        self.column_widgets = []

    def save(filepath):
        pass