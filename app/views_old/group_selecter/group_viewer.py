import ui
from app.views.abstract_viewer import AbstractViewer
import app.views.group_selecter.group_data_source as group_data_source
import app.views.group_selecter.group_delegate as group_delegate

"""
Displays a TableView [https://omz-software.com/pythonista/docs/ios/ui.html#tableview] from a list AppData.groups
When a row in the table is selected
- the row index is stroed in AppData.selected_group_index
- the view closes
"""
class GroupViewer(AbstractViewer):
    def __init__(self, parent_view, app_data):
        super().__init__(parent_view, app_data)

    def show(self):
        tv_data_source = group_data_source.GroupDataSource(self.app_data)
        self.tv.data_source = tv_data_source
        tv_delegate = group_delegate.GroupDelegate(self.app_data)
        self.tv.delegate = tv_delegate
        self.tv.name = 'Select Group'
        super().show()
