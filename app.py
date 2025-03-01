import time
import app.data.data_loader as data_loader
from app.views.parent.parent_view import ParentView
from app.ui.group_selecter import GroupSelecter
import app.data.app_data as app_data

def run():
	pv = ParentView()
	ad = app_data.AppData(None)
	dl = data_loader.DataLoader()
	ad.groups = dl.load_groups()
	
run()
