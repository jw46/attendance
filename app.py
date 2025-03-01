import sys
import importlib
import app.data.app_data as app_data
import app.data.loader as loader
import app.apputil.util as util

def run():
	menu_filepath = util.get_parent_path() + 'metadata/menu.csv'
	menu_df = loader.open_df(menu_filepath)
	while app_data.selected_group != 'exit':
		module_string = menu_df.loc[menu_df['menu'] == app_data.current_ui, 'controller'].item()
		if module_string is None:
			sys.exit()
		module = None
		try:
			module = importlib.import_module(module_string)
		except:
			sys.exit()
		module.Controller()
run()
