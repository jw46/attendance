import ui

class ViewWithBarAndTable(ui.View):
    def __init__(self, app_data):
        self.button_height_percent = 15
        self.app_data = app_data

    def add_table(self, df):
        self.tv = ui.TableView()
        screen_size = ui.get_screen_size()
        self.tv.width = int(screen_size[0])
        self.tv.height = int(screen_size[1] * (100 - self.button_height_percent) / 110)
        self.tv.y = int(screen_size[1] * self.button_height_percent / 110)
        self.tv.x = 0
        self.add_subview(self.tv)

    def add_bar(self, bar_text):
        screen_size = ui.get_screen_size()
        self.bar = ui.Label()
        self.bar.width = int(screen_size[0])
        self.bar.x = 0
        self.bar.height = int(screen_size[1] * self.button_height_percent / 110)
        self.bar.y = 0
        self.bar.border_width = 0.5
        self.bar.background_color = '#AAAAAA'
        self.bar.font = (self.bar.font[0] ,60)
        self.bar.text = bar_text
        self.add_subview(self.bar)
