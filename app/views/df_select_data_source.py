import ui

class DfselectDataSource (AbstractDataSource):
    def __init__(self, view, df):
        self.view = view
        self.df = self

    def get_column_widths(self):
        max_lengths = list(map(lambda x: (x, int(self.df[x].str.len().max())), self.df.columns))
        item_widths = list(map(lambda x: (x[0], int(x[1] / sum(max_lengths) * ui.screen_size[0]), ), max_lengths))
        return list(map(lambda x: (x, sum(x[1][:self.df.columns.index(x[0] -1)])), item_widths))

    def tableview_number_of_rows(self, tableview, section):
        return len(self.app_data.students_df.index) -1

    def add_values(self, column, row):

    def tableview_cell_for_row(self, tableview, section, row):
        cell = ui.TableViewCell()
        cell.bounds = (0, 0, tableview.width, tableview.row_height)
