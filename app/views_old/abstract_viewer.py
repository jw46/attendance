from abc import ABC, abstractmethod
import ui_old
"""

"""
class AbstractViewer(ABC):
    def __init__(self, parent_view, app_data, has_close_button: bool=False):
        self.button_height_percent = 15
        self.has_close_button = has_close_button
        self.app_data = app_data
        self.pv = parent_view
        self.tv = ui_old.TableView()
        screen_size = ui_old.get_screen_size()
        self.tv.width = int(screen_size[0])
        self.tv.height = int(screen_size[1] * (100 - self.button_height_percent) / 110)
        self.tv.y = int(screen_size[1] * self.button_height_percent / 110)
        self.tv.x = 0
        if has_close_button:
            self.with_close_button(screen_size)
        self.add_info_label(screen_size)

    def add_info_label(self, screen_size):
        self.info_label = ui_old.Label()
        if self.has_close_button:
            self.info_label.width = 200 - int(screen_size[0])
            self.info_label.x = 200
        else:
            self.info_label.width = int(screen_size[0])
            self.info_label.x = 0
        self.info_label.height = int(screen_size[1] * self.button_height_percent / 110)
        self.info_label.y = 0
        self.info_label.border_width = 0.5
        self.info_label.background_color = '#AAAAAA'
        self.info_label.font = (self.info_label.font[0] ,60)
        self.info_label.text = self.app_data.selected_group[20:-15] + '    ' + self.app_data.selected_date

    def close_button_clicked(self, sender):
        pass

    def with_close_button(self, screen_size):
        self.close_button = ui_old.Button(title='Done')
        self.close_button.action = self.close_button_clicked
        self.close_button.width = 200
        self.close_button.height = int(screen_size[1] * self.button_height_percent / 110)
        self.close_button.x = 0
        self.close_button.y = 0
        self.close_button.border_width = 0.5
        self.close_button.background_color = '#333333'
        self.close_button.font = (self.close_button.font[0] ,60)

    def without_close_button(self, screen_size):
        self.tv.height = int(screen_size[1] * 9/10)

    def show(self):
        self.pv.add_subview(self.tv)
        self.pv.add_subview(self.info_label)
        if self.has_close_button:
            self.pv.add_subview(self.close_button)

    def close(self):
        self.pv.remove_subview(self.tv)
        self.pv.remove_subview(self.info_label)
        if self.has_close_button:
            self.pv.remove_subview(self.close_button)

    
