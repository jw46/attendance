import time
import app.data.groups_loader as groups_loader
import app.views.parent.parent_view as parent_view
from app.views.group_selecter.group_viewer import GroupViewer
from app.views.student_selecter.student_viewer import StudentViewer

class GroupSelecter():
	def __init__(self, app_data):
		self.app_data = app_data
		
	def run(self, pv):
		print('run')
		gv = GroupViewer(pv, self.app_data)
		print(gv)
		gv.show()
		self.app_data.selected_group_index = -1
		while self.app_data.selected_group_index == -1:
			time.sleep(0.1)
			self.app_data.selected_group = self.app_data.groups[self.app_data.selected_group_index]
		gv.close()
		self.app_data.current_ui = 'Menu'
