import ui

"""
A data source for the TableView [https://omz-software.com/pythonista/docs/ios/ui.html#tableview]
Uses AppData.groups to populate the TableView
"""
class GroupDataSource (object):
    def __init__(self, app_data):
        self.app_data = app_data

    def tableview_number_of_sections(self, tableview):
        # Return the number of sections (defaults to 1)
        return 1

    def tableview_number_of_rows(self, tableview, section):
        # Return the number of rows in the section
        len(self.app_data.class_df.index) -1

    """
    Populates a TableView row
    """
    def tableview_cell_for_row(self, tableview, section, row):
        cell = ui.TableViewCell()
        cell.bounds = (0, 0, tableview.width, tableview.row_height)

        date_label = ui.Label()
        date_label.border_width = 0.5
        date_label.text = self.app_data.class_df['Class Dates'][row]
        date_label.frame = (0, 0, 300, tableview.row_height)
        date_label.alignment = ui.ALIGN_LEFT
        cell.content_view.add_subview(date_label)

        class_label = ui.Label()
        class_label.border_width = 0.5
        class_label.text = self.app_data.class_df['Class Title'][row]
        class_label.frame = (300, 0, tableview.width  - 300, tableview.row_height)
        class_label.alignment = ui.ALIGN_LEFT
        cell.content_view.add_subview(class_label)
        return cell

    def tableview_title_for_header(self, tableview, section):
        # Return a title for the given section.
        # If this is not implemented, no section headers will be shown.
        return 'Groups'

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