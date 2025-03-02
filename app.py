import sys
import importlib
import app.data.app_data as app_data
import app.data.loader as loader
import app.apputil.util as util

def run():
    app_data.selected_date = util.get_today()
    menu_df = loader.open_df(util.get_menu_filepath())
    while app_data.selected_group != 'exit':
        module_string = menu_df.loc[menu_df['menu'] == app_data.current_ui, 'controller'].item()
        if module_string is None:
            sys.exit()
        module = None
        module = importlib.import_module(module_string)
        module.Controller()
run()
