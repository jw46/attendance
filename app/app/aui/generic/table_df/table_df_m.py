import pandas as pd
import app.apputil.util as util

class TableDfModel:
    def __init__(self, source_filepath):
        self.source_filepath = source_filepath
        if self.source_filepath:
            self.df = pd.read_csv(self.source_filepath, dtype=str, sep=';', quotechar='"')
            self.columns = self.df.columns
        self.label_text = util.get_bar_text()
        self.column_widgets = []

    def save(filepath):
        pass