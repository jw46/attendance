import time
import app.data.data_loader as data_loader
import app.views.parent.parent_view as parent_view
from app.views.class_view.class_viewer import ClassViewer
from app.views.student_selecter.student_viewer import StudentViewer

class DateSelecter():
	def __init__(self, app_data):
		self.app_data = app_data

	def run(self, pv):
		print('run')
		cv = ClassViewer(pv, self.app_data)
		cv.show()
		while self.app_data.current_ui != 'Menu':
			time.sleep(0.1)
		cv.close()
