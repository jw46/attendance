import time
from app.data.class_loader import ClassLoader
from app.views.class_view.class_viewer import ClassViewer

class DateSelecter():
	def __init__(self, app_data):
		self.app_data = app_data

	def run(self, pv):
		try:
			cl = ClassLoader()
			cl.load(self.app_data)
		except:
			self.app_data.alert_text = 'No class file found, please check your configuration'
			self.app_data.current_ui = 'Alert'
			self.app_data.next_ui = 'Select a different group'
			return
		cv = ClassViewer(pv, self.app_data)
		cv.show()
		while self.app_data.current_ui != 'Menu':
			time.sleep(0.1)
		cv.close()
		
			