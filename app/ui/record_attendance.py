import time
import pandas as pd
import numpy as np
from app.ui.abstract_ui import AbstractUI
from app.views.parent.parent_view import ParentView
from app.views.student_selecter.student_viewer import StudentViewer
from app.data.data_loader import DataLoader
import app.apputil.config as config

"""
Pythonista iOS UI application for recording student attendance in class
"""
class RecordAttendance(AbstractUI):
	def __init__(self, app_data):
		super().__init__(app_data)
		
	def run(self, pvo):
		dl = DataLoader()
		df = dl.get_students(self.app_data.selected_group)
		self.app_data.sc_object = [None] * len(df.index)
		if not config.ATTENDANCE_COLUMN_NAME in df:
			df[config.ATTENDANCE_COLUMN_NAME] = pd.Series(dtype='str')
		if not config.NAME_COLUMN_NAME in df:
			df = df.assign(name=np.where(df.imie2.isnull(), df.imie + ' ' + df.nazwisko, df.imie + ' ' + df.imie2 + ' ' + df.nazwisko))
		self.app_data.students_df = df
		pv = ParentView()
		sv = StudentViewer(pv, self.app_data)
		sv.show()
		# while self.app_data.current_ui != 'Menu':
		# 	time.sleep(0.1)
		

