import pandas as pd
from app.aui.generic.table_df.table_df_m import TableDfModel
import app.apputil.config as config
import app.data.app_data as app_data
import app.apputil.util as util

class Model(TableDfModel):
    def __init__(self, source_filepath):
        super().__init__(source_filepath)
        self.column_widgets = [('menu', 'label')]
        self.visible_columns = list(map(lambda x: x[0], self.column_widgets))
        self.button_text = config.STANDARD_BUTON_TEXT
        self.table_name = 'Menu'