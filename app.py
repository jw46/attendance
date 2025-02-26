import time
import app.data.data_loader as data_loader
from app.views.parent.parent_view import ParentView
from app.ui.group_selecter import GroupSelecter
import app.data.app_data as app_data

def run():
	pv = ParentView()
	ad = app_data.AppData(pv)
	dl = data_loader.DataLoader()
	ad.groups = dl.load_groups()
	pv.present('fullscreen')
	while ad.current_ui != 'Quit app':
		current_ui = ad.menu[ad.current_ui]
		current_ui.run(pv)
		ad.waiting = True
		while not ad.waiting:
			time.sleep(0.1)
	pv.close()
	
run()
