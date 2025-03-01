"""
Deletage to the TableView [https://omz-software.com/pythonista/docs/ios/ui.html#tableview]
"""
class GroupDelegate (object):
    def __init__(self, app_data):
        self.app_data = app_data

    """
    Sets AppData.selected_group_index to the index of the row selected by the user and closes the View
    """
    def tableview_did_select(self, tableview, section, row):
        self.app_data.selected_group_index = int(row)
        tableview.close()

    def tableview_did_deselect(self, tableview, section, row):
        # Called when a row was de-selected (in multiple selection mode).
        pass

    def tableview_title_for_delete_button(self, tableview, section, row):
        # Return the title for the 'swipe-to-***' button.
        return 'Delete'

    # def tableview_accessory_button_tapped(self, tableview, section, row):