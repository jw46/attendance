import ui

"""
A data source for the TableView [https://omz-software.com/pythonista/docs/ios/ui.html#tableview]
Uses AppData.menus to populate the TableView
"""
class MenuDataSource (object):
    def __init__(self, app_data):
        self.app_data = app_data
        self.menu_list = list(self.app_data.menu.keys())

    def tableview_number_of_sections(self, tableview):
        # Return the number of sections (defaults to 1)
        return 1

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

    def tableview_can_delete(self, tableview, section, row):
        # Return True if the user should be able to delete the given row.
        return True

    def tableview_can_move(self, tableview, section, row):
        # Return True if a reordering control should be shown for the given row (in editing mode).
        return True

    def tableview_delete(self, tableview, section, row):
        # Called when the user confirms deletion of the given row.
        pass

    def tableview_move_row(self, tableview, from_section, from_row, to_section, to_row):
        # Called when the user moves a row with the reordering control (in editing mode).
        pass
