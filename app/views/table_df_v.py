import ui


class TableDfView:
    def __init__(self, model):
        self.model = model
        tv = ui.TableView()
        self.column_x_widths = self.get_column_x_widths()

    def get_item_widths(self, l):
        return sum(list(map(lambda x: x[1], l)))

    def get_left(self, l, x):
        max_index = list(self.model.df.columns).index(x[0])
        sub_list = l[:max_index]
        return self.get_item_widths(sub_list)

    def get_column_x_widths(self):
        max_lengths = list(map(lambda x: (x, int(self.model.df[x].str.len().max())), self.model.df.columns))
        item_widths = list(map(lambda x: (x[0], int(x[1] / self.get_item_widths(max_lengths) * ui.get_screen_size()[0])), max_lengths))
        # return item_widths
        return list(map(lambda x: {x[0], (x[1], self.get_left(item_widths, x))}, item_widths))

    def tableview_number_of_rows(self, tableview, section):
        return len(self.app_data.students_df.index) -1

    def add_label(self, cell, row, column_name):
        label = ui.Label(text=self.model.df[column_name].loc[row])
        return label
        

    def add_text_field(self, cell, row, column_name):
        tf = ui.TextField(text=self.model.df[column_name].loc[row])
        return tf

    def add_widgets(self, cell, row):
        for c in self.model.column_widgets:
            if c[1] == 'label':
                widget = self.add_label(cell, row, c[0])
            if c[1] == 'text_field':
                widget = self.add_text_field(cell, row, c[0])
            widget.x = self.column_x_widths[c[0]][1]
            widget.width = self.column_x_widths[c[0]][0]
            widget.y = 0
            widget.height = cell.height
            cell.add_subview(widget)
    

    def tableview_cell_for_row(self, tableview, section, row):
        cell = ui.TableViewCell()
        cell.bounds = (0, 0, tableview.width, tableview.row_height)
        self.add_widgets(cell, row)



