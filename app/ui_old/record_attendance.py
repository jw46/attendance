import pandas as pd
from app.views.student_selecter.student_viewer import StudentViewer
from app.data.groups_loader import DataLoader
import app.apputil.config as config

"""
Pythonista iOS UI application for recording student attendance in class
"""
class RecordAttendance():
	def __init__(self, app_data):
		self.app_data = app_data
		
	def run(self, pv):
		dl = DataLoader()
		self.app_data.students = dl.get_students(self.app_data.selected_group)
		self.app_data.sc_object = [None] * len(self.app_data.students.index)
		if not config.ATTENDANCE_COLUMN_NAME in self.app_data.students:
			self.app_data.students[config.ATTENDANCE_COLUMN_NAME] = pd.Series(dtype='str')
		sv = StudentViewer(pv, self.app_data)
		sv.show()

