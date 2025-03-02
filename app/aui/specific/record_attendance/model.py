import pandas as pd
import app.apputil.config as config
import app.data.app_data as app_data
import app.data.att_loader as al
from app.aui.generic.table_df_bar.table_df_bar_m import TableDfBarModel

class Model(TableDfBarModel):
    def __init__(self, source_filepath):
        super().__init__(source_filepath)
        self.df = al.load()
        self.column_widgets = [('name', 'label')]
        self.button_text = config.STANDARD_BUTON_TEXT
        self.table_name = 'Select a student'
