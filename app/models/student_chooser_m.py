import pandas as pd
from app.models.table_df_m import TableDfModel

class StudentChooserModel(TableDfModel):
    def __init__(self, source_filepath):
        super().__init__(source_filepath)
        self.column_widgets = [
                # ('nazwisko', 'label'), 
                # ('imie', 'label'), 
                # ('imie2', 'label'), 
                # ('skreslony', 'label'), 
                # ('rezygnacja', 'label'), 
                # ('email', 'label'), 
                # ('indeks', 'label'), 
                # ('attendence', 'label'), 
                ('name', 'label')
            ]
