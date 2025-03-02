from app.aui.generic.table_df_bar.table_df_bar_v import TableDfBarView

class View(TableDfBarView):
    def __init__(self, model, controller):
        super().__init__(model, controller)
        self.tv.allows_selection = False
