import ui

class TableDfView(ui.View):
    def __init__(self, model):
        self.model = model
        self.tv = ui.TableView()
        self.add_subview(self.tv)
