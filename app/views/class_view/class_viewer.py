import ui
from app.views.abstract_viewer import AbstractViewer
from app.views.class_view.class_data_source import ClassDataSource
from app.views.class_view.date_delegate import DateDelegate
import app.data.class_saver as class_saver

"""
Displays a TableView [https://omz-software.com/pythonista/docs/ios/ui.html#tableview] from a list AppData.groups

"""
class ClassViewer(AbstractViewer):
    def __init__(self, parent_view, app_data, is_class_editor=False):
        super().__init__(parent_view, app_data, has_close_button=is_class_editor)
        self.is_class_editor = is_class_editor

    def close_button_clicked(self, sender):
        if self.is_class_editor:
            self.app_data.current_ui = 'Menu'
            class_saver.save(self.app_data.class_df, self.app_data.selected_group)
            self.tv.close()

    def show(self):
        tv_data_source = ClassDataSource(self.app_data, self.is_class_editor)
        self.tv.data_source = tv_data_source
        tv_delegate = DateDelegate(self.app_data, self.is_class_editor)
        self.tv.delegate = tv_delegate
        self.tv.name = 'Classes'
        super().show()
