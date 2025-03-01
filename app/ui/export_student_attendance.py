import time
from app.data.data_loader import DataLoader
import app.views.parent.parent_view as parent_view
from app.views.student_selecter.student_viewer import StudentViewer

class ExportStudentAttendance():
	def __init__(self, app_data):
		self.app_data = app_data

	def run(self, pv):
		dl = DataLoader()
		self.app_data.students_df = dl.get_students(self.app_data.selected_group)
		cv = StudentViewer(pv, self.app_data, True)
		cv.show()
		while self.app_data.current_ui != 'Menu':
			time.sleep(0.1)
		cv.close()
