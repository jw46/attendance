import sys
import importlib
import ui
import app.data.app_data as app_data
import app.data.loader as loader
import app.apputil.util as util

def run():
    app_data.selected_date = util.get_today()
    menu_df = loader.open_df(util.get_menu_filepath())
    app_view = ui.ScrollView()
    app_view.shows_vertical_scroll_indicator = True
    app_view.flex = 'WHTL'
    app_view.present('fullscreen')
    while app_data.selected_group != 'exit':
        module_string = menu_df.loc[menu_df['menu'] == app_data.current_ui, 'controller'].item()
        if module_string is None:
            sys.exit()
        module = None
        module = importlib.import_module(module_string)
        module.Controller(app_view)
run()
