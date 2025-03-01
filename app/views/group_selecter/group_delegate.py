from app.views.abstract_delegate import AbstractDelegate
"""
Deletage to the TableView [https://omz-software.com/pythonista/docs/ios/ui.html#tableview]
"""
class GroupDelegate (AbstractDelegate):
    def __init__(self, app_data, pv):
        super().__init__(app_data, pv)

    """
    Sets AppData.selected_group_index to the index of the row selected by the user and closes the View
    """
    def tableview_did_select(self, tableview, section, row):
        self.app_data.selected_group_index = int(row)
        self.pv.close()
