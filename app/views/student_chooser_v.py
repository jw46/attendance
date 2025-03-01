import ui
from app.views.table_df_v import TableDfView

class StudentChooserView(TableDfView):
    def __init__(self, model):
        super().__init__(model)
        self.tv.allows_selection = True
        
        

    