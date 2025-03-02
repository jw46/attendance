from app.aui.generic.table_df.table_df_ds import TableDfDataSource

class DataSource(TableDfDataSource):
    def __init__(self, model, table_size):
        super().__init__(model, table_size)

    def widget_action(self, sender):
        widget_location = self.get_widget_location(sender)
        self.model.df[widget_location[1]].loc[widget_location[0]] = sender.text