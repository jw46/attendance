import pandas as pd
import app.apputil.util as util
# from app.ui_old.record_attendance import RecordAttendance
# from app.ui_old.group_selecter import GroupSelecter
# from app.ui_old.class_title_editor import ClassTitleEditor
# from app.ui_old.date_selecter import DateSelecter
# from app.ui_old.export_spreadsheet import ExportSpreadsheet
# from app.ui_old.export_student_attendance import ExportStudentAttendance
# from app.ui_old.edit_students import EditStudent
# from app.ui_old.backup_data import BackupData
# from app.ui_old.quit_app import QuitApp
# from app.ui_old.menu import Menu

class AppData:
    def __init__(self, parent_view):
        self.groups: list[str] = None
        self.selected_group_index: int = -1
        self.selected_group: str = 'No group selected'
        self.selected_date = util.get_today()
        self.students_df: pd.DataFrame = None
        self.class_df: pd.DataFrame = None
        self.sc_object = None
        self.menu = {
        		# 'Select a different group': GroupSelecter(self),
        		# 'Record attendance': RecordAttendance(self),
        		# 'Change date': DateSelecter(self),
        		# 'Record class title': ClassTitleEditor(self),
        		# 'Export spreadsheet': ExportSpreadsheet(self),
        		# 'Export student attendance': ExportStudentAttendance(self),
        		# 'Edit students': EditStudent(self),
                # 'Backup data': BackupData(self),
        		# 'Quit app': QuitApp(self),
        		# 'Menu': Menu(self)
        	}
        self.current_ui: str = 'Select a different group'
        self.waiting = False
