import ui_old
import app.views.abstract_viewer as abstract_viewer
import app.views.student_selecter.student_data_source as student_data_source
import app.views.student_selecter.student_delegate as student_delegate
from app.data.data_saver import DataSaver
import app.apputil.config as config

class StudentViewer(abstract_viewer.AbstractViewer):
    def __init__(self, parent_view, app_data):
        super().__init__(parent_view, app_data, has_close_button=True)

    def close_button_clicked(self, sender):
        data_saver = DataSaver()
        data_saver.save_attendence(self.app_data.students, self.app_data.selected_group)
        self.tv.close()
        self.app_data.waiting = False
        self.app_data.current_ui = 'Menu'

    def show(self):
        self.tv.row_height = 30
        self.tv.allows_selection = False
        tv_data_source = student_data_source.StudentDataSource(self.app_data)
        self.tv.data_source = tv_data_source
        tv_delegate = student_delegate.StudentDelegate(self.app_data)
        self.tv.delegate = tv_delegate
        self.tv.name = 'Select student'
        super().show()
