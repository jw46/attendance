import ui

class TableDfView(ui.View):
    def __init__(self, model, controller):
        self.model = model
        self.controller = controller
        self.tv = ui.TableView()
        table_size = (ui.get_screen_size()[0],int(ui.get_screen_size()[1]))
        self.tv.width = table_size[0]
        self.tv.height = table_size[1]
        self.add_subview(self.tv)
