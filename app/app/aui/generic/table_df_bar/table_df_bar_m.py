import pandas as pd
from app.aui.generic.table_df.table_df_m import TableDfModel

class TableDfBarModel(TableDfModel):
    def __init__(self, source_filepath):
        super().__init__(source_filepath)