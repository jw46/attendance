import ui
from app.views.abstract_data_source import AbstractDataSource

"""
A data source for the TableView [https://omz-software.com/pythonista/docs/ios/ui.html#tableview]
Uses AppData.menus to populate the TableView
"""
class MenuDataSource (AbstractDataSource):
    def __init__(self, app_data):
        super().__init__(app_data)
        self.menu_list = list(self.app_data.menu.keys())

    def tableview_number_of_rows(self, tableview, section):
        # Return the number of rows in the section
        return len(self.app_data.menu) - 1

    """
    Populates a TableView row
    """
    def tableview_cell_for_row(self, tableview, section, row):
        # Create and return a cell for the given section/row
        cell = ui.TableViewCell()
        cell.text_label.text = self.menu_list[row]
        cell.text_label.font = (cell.text_label.font[0] ,40)
        return cell

    def tableview_title_for_header(self, tableview, section):
        # Return a title for the given section.
        # If this is not implemented, no section headers will be shown.
        return 'Menu'
