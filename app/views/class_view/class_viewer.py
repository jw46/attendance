import ui
from app.views.abstract_viewer import AbstractViewer
from app.views.class_view.class_data_source import ClassDataSource
from app.views.class_view.date_delegate_delegate import DateDelegate

"""
Displays a TableView [https://omz-software.com/pythonista/docs/ios/ui.html#tableview] from a list AppData.groups

"""
class ClassViewer(AbstractViewer):
    def __init__(self, parent_view, app_data, is_class_editor=False):
        super().__init__(parent_view, app_data)
        self.is_class_editor = is_class_editor

    def close_button_clicked(self, sender):
        pass

    def show(self):
        tv_data_source = ClassDataSource(self.app_data)
        self.tv.data_source = tv_data_source
        if not self.is_class_editor:
            tv_delegate = DateDelegate(self.app_data)
            self.tv.delegate = tv_delegate
        self.tv.name = 'Select Group'
        super().show()
