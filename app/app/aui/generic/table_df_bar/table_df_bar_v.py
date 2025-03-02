import ui
from app.aui.generic.table_df.table_df_v import TableDfView

class TableDfBarView(TableDfView):
    def __init__(self, model, controller):
        super().__init__(model, controller)
        self.table_size = (ui.get_screen_size()[0],int(ui.get_screen_size()[1] * 0.85))
        self.tv.width = self.table_size[0]
        self.tv.height = int(self.table_size[1] * 0.85)
        self.tv.y =  75
        self.add_info_label()
        self.add_close_button()

    def add_close_button(self):
        self.close_button = ui.Button(title=self.model.button_text)
        self.close_button.action = self.close_button_clicked
        self.close_button.width = 200
        self.close_button.height = 75
        self.close_button.x = 0
        self.close_button.y = 0
        self.close_button.border_width = 0.5
        self.close_button.background_color = '#333333'
        self.close_button.font = (self.close_button.font[0] ,40)
        self.add_subview(self.close_button)

    def add_info_label(self):
        self.info_label = ui.Label()
        self.info_label.width = 200 - int(self.table_size[0])
        self.info_label.x = 200
        self.info_label.height = 75
        self.info_label.y = 0
        self.info_label.border_width = 0.5
        self.info_label.background_color = '#AAAAAA'
        self.info_label.font = (self.info_label.font[0] ,40)
        self.info_label.text = self.model.label_text
        self.add_subview(self.info_label)

    def close_button_clicked(self, sender):
        self.controller.app_view.remove_subview(self)
