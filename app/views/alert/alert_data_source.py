import ui
from app.views.abstract_data_source import AbstractDataSource

"""
Making a one row table as a workaround, need a new super class for the view
"""
class AlertDataSource (AbstractDataSource):
    def __init__(self, app_data):
        super().__init__(app_data)

    def tableview_number_of_rows(self, tableview, section):
        # Return the number of rows in the section
        return 1

    """
    Populates a TableView row
    """
    def tableview_cell_for_row(self, tableview, section, row):
        # Create and return a cell for the given section/row
        cell = ui.TableViewCell()
        cell.text_label.text = self.app_data.alert_text
        cell.text_label.font = (cell.text_label.font[0], 40)
        return cell

    def tableview_title_for_header(self, tableview, section):
        # Return a title for the given section.
        # If this is not implemented, no section headers will be shown.
        return 'Alert'
