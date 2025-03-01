from app.aui.generic.table_df_bar.table_df_bar_v import TableDfBarView

class StudentChooserView(TableDfBarView):
    def __init__(self, model):
        super().__init__(model)
        self.tv.allows_selection = True

    def close_button_clicked(self, sender):
        pass
        
        

    