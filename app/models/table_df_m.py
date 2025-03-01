import pandas as pd

class TableDfModel:
    def __init__(self, source_filepath):
        self.source_filepath = source_filepath
        self.df = pd.read_csv(self.source_filepath, dtype=str, sep=';', quotechar='"')
        columns = self.df.columns
        self.column_widgets = [
                ('nazwisko', 'label'), 
                ('imie', 'label'), 
                ('imie2', 'label'), 
                ('skreslony', 'label'), 
                ('rezygnacja', 'label'), 
                ('email', 'label'), 
                ('indeks', 'label'), 
                ('attendence', 'label'), 
                ('name', 'label')
            ]

    def save(filepath):
        pass