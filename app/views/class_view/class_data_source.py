import ui
import pandas as pd
from app.views.abstract_data_source import AbstractDataSource
import app.apputil.config as config

"""
A data source for the TableView [https://omz-software.com/pythonista/docs/ios/ui.html#tableview]
Uses AppData.groups to populate the TableView
"""
class ClassDataSource (AbstractDataSource):
    def __init__(self, app_data, is_class_editor=False):
        super().__init__(app_data)
        self.is_class_editor = is_class_editor
        self.class_titles = {1: [None] * (len(self.app_data.class_df.index) + 1), 2: [None] * (len(self.app_data.class_df.index) + 1)}


    def tableview_number_of_rows(self, tableview, section):
        return len(self.app_data.class_df.index)

    def class_title_action1(self, sender):
        self.class_title_action(sender, 1)

    def class_title_action2(self, sender):
        self.class_title_action(sender, 2)
    
    def class_title_action(self, sender, title_number):
        row = self.class_titles[title_number].index(sender)
        self.app_data.class_df.at[row, config.CLASS_TITLE_COLUMN_NAME[title_number]] = sender.text
    
    def add_class_title(self, row, height, title_number):
        if self.is_class_editor:
            class_widget = ui.TextField()
        else:
            class_widget = ui.Label()
        class_widget.border_width = 0.5
        if str(self.app_data.class_df[config.CLASS_TITLE_COLUMN_NAME[title_number]][row]) == 'nan':
            class_widget.text = ''
        else:
            class_widget.text = str(self.app_data.class_df[config.CLASS_TITLE_COLUMN_NAME[title_number]][row])
        class_widget.width = int(ui.get_screen_size()[0]  * 7/20)
        class_widget.height = int(height)
        class_widget.x = int(ui.get_screen_size()[0]  * (3/10 + (title_number -1) * 7/20))
        class_widget.y = 0
        class_widget.alignment = ui.ALIGN_LEFT
        if title_number == 1:
            class_widget.action = self.class_title_action1
        else:
            class_widget.action = self.class_title_action2
        self.class_titles[title_number][row] = class_widget
        return class_widget

    """
    Populates a TableView row
    """
    def tableview_cell_for_row(self, tableview, section, row):
        cell = ui.TableViewCell()
        cell.bounds = (0, 0, tableview.width, 50)#tableview.row_height)
        date_label = ui.Label()
        date_label.border_width = 0.5
        date_label.text = self.app_data.class_df[config.CLASS_DATES_COLUMN_NAME][row]
        date_label.width = int(tableview.width  * 3/10)
        date_label.height = int(cell.height)
        date_label.x = 0
        date_label.y = 0
        # date_label.alignment = ui.ALIGN_LEFT
        cell.content_view.add_subview(date_label)
        cell.content_view.add_subview(self.add_class_title(row, cell.height, 1))
        cell.content_view.add_subview(self.add_class_title(row, cell.height, 2))
        return cell

    def tableview_title_for_header(self, tableview, section):
        return 'Classes'
