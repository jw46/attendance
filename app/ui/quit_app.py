import time
import sys
import app.data.data_loader as data_loader
import app.views.parent.parent_view as parent_view
from app.views.alert.alert_viewer import AlertViewer

class QuitApp():
	def __init__(self, app_data):
		self.app_data = app_data

	def run(self, pv):
		# self.app_data.current_ui = 'Alert'
		# self.app_data.current_ui = 'Die'
		# cv = AlertViewer(pv, self.app_data)
		# cv.show()
		# while self.app_data.current_ui == 'Alert':
		# 	time.sleep(0.1)
		# if self.app_data.current_ui == 'Die':
		# cv.close()
		sys.exit()
