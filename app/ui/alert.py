import time
from app.views.alert.alert_viewer import AlertViewer

class Alert():
	def __init__(self, app_data):
		self.app_data = app_data
		
	def run(self, pv):

		av = AlertViewer(pv, self.app_data)
		av.show()
		while self.app_data.current_ui == "Alert":
			time.sleep(0.1)
		av.close()
