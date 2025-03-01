import ui
from app.aui.generic.table_df.table_df_ds import TableDfDataSource

class TableDfBarDataSource (TableDfDataSource):
    def __init__(self, model, table_size):
        super().__init__(model, (table_size[0], table_size[1] - 75))