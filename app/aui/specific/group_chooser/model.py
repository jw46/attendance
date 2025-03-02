import pandas as pd
import app.apputil.config as config
import app.data.app_data as app_data
import app.data.groups_loader as gl
import app.data.app_data as app_data
from app.aui.generic.table_df_bar.table_df_bar_m import TableDfBarModel

class Model(TableDfBarModel):
    def __init__(self, source_filepath = None):
        super().__init__(source_filepath)
        self.df = gl.get_group_names()
        self.column_widgets = [('Groups', 'label')]
        self.button_text = config.STANDARD_BUTON_TEXT
        self.table_name = 'Choose Group'
