import pandas as pd
from app.aui.generic.table_df.table_df_m import TableDfModel
import app.apputil.config as config
import app.data.app_data as app_data

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
        self.button_text = config.STANDARD_BUTON_TEXT
        self.label_text = 'test'
