import time
from app.ui.abstract_ui import AbstractUI
from app.views.parent.parent_view import ParentView
from app.views.group_selecter.group_viewer import GroupViewer
from app.views.student_selecter.student_viewer import StudentViewer

class GroupSelecter(AbstractUI):
	def __init__(self, app_data):
		super().__init__(app_data)
		
	def run(self):
		gv = GroupViewer(self.pv, self.app_data)
		self.app_data.selected_group_index = -1
		gv.show()
		gv.close()
		super().run()
		self.app_data.current_ui = 'Menu'
