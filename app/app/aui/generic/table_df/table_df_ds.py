import pandas as pd
import ui
from app.aui.generic.abstract_data_source import AbstractDataSource

class TableDfDataSource (AbstractDataSource):
    def __init__(self, model, table_size):
        super().__init__(model)
        self.table_size = table_size
        self.column_x_widths = self.get_column_x_widths()
        self.widget_list = [ {} for _ in range(len(self.model.df.index))]

    def get_item_widths(self, l):
        return sum(list(map(lambda x: x[1], l)))

    def get_left(self, l, x):
        max_index =self.model.visible_columns.index(x[0])
        sub_list = l[:max_index]
        return self.get_item_widths(sub_list)

    def get_max_column_chars(self, x):
        num_chars = self.model.df[x].str.len().max()
        if pd.isna(num_chars) or num_chars == 0:
            return 30
        return int(num_chars)

    def get_column_x_widths(self):
        max_lengths = list(map(lambda x: (x, self.get_max_column_chars(x)), self.model.visible_columns))
        item_widths = list(map(lambda x: (x[0], int(x[1] / self.get_item_widths(max_lengths) * ui.get_screen_size()[0])), max_lengths))
        l = list(map(lambda x: (x[0], x[1], self.get_left(item_widths, x)), item_widths))
        return {a:(b,c) for a,b,c in l}
    
    def tableview_number_of_rows(self, tableview, section):
        return len(self.model.df)

    def add_label(self, row, column_name):
        label = ui.Label(text=str(self.model.df[column_name].loc[row]))
        return label 

    def add_text_field(self, row, column_name):
        tf = ui.TextField(text=str(self.model.df[column_name].loc[row]))
        return tf

    """
    Finds the location in the dataframe of the ui widget
    """
    def get_widget_location(self, sender):
        count = 0
        for i in self.widget_list:
            for k,v in i.items():
                if v == sender:
                    return (count, k)
            count = count + 1

    def widget_action(self, sender):
        widget_location = self.get_widget_location(sender)

    def add_widgets(self, cell, row):
        for c in self.model.column_widgets:
            if c[1] == 'label':
                widget = self.add_label(row, c[0])
            if c[1] == 'text_field':
                widget = self.add_text_field(row, c[0])
                widget.action = self.widget_action
            widget.x = self.column_x_widths[c[0]][1]
            widget.width = self.column_x_widths[c[0]][0]
            widget.y = 0
            widget.height = 50
            widget.alignment = ui.ALIGN_LEFT
            self.widget_list[row][c[0]] = widget
            cell.add_subview(widget)

    def tableview_cell_for_row(self, tableview, section, row):
        cell = ui.TableViewCell()
        cell.bounds = (0, 0, self.table_size[0], 50)
        self.add_widgets(cell, row)
        return cell

    def tableview_title_for_header(self, tableview, section):
        if self.model.table_name:
            return self.model.table_name
        return 'Table from DataFrame'
