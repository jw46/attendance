from app.views.abstract_delegate import AbstractDelegate
import app.apputil.config as config
from app.data.export_student_attendance import ExportStudentAttendance

class StudentDelegate (AbstractDelegate):
    def __init__(self, app_data, pv):
        super().__init__(app_data)
        self.pv = pv

    def tableview_did_select(self, tableview, section, row):
        self.app_data.selected_student = self.app_data.students_df[config.NAME_COLUMN_NAME].loc[row]
        xsa = ExportStudentAttendance(self.app_data, self.pv)
        xsa.export()
        self.pv.close()
        self.app_data.current_ui = 'Quit app'
