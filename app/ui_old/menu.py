import time
from app.views.menu.menu_viewer import MenuViewer

class Menu():
	def __init__(self, app_data):
		self.app_data = app_data
		
	def run(self, pv):
		mv = MenuViewer(pv, self.app_data)
		mv.show()
		while self.app_data.current_ui == 'Menu':
			time.sleep(0.1)
		mv.close()
