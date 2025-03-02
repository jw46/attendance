import pandas as pd
import app.apputil.config as config
import app.data.app_data as app_data
import app.data.class_loader as cl
import app.data.app_data as app_data
from app.aui.generic.table_df_bar.table_df_bar_m import TableDfBarModel

class Model(TableDfBarModel):
    def __init__(self, source_filepath=None):
        super().__init__(source_filepath)
        self.df = cl.load()
        self.column_widgets = [('Class Dates', 'label'), ('Class Title', 'text_field')]
        self.button_text = config.STANDARD_BUTON_TEXT
        self.table_name = 'Choose Class Date'
