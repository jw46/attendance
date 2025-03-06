import time
import app.apputil.export_to_spreadsheet as xts
import app.data.app_data as app_data

class Controller:
    def __init__(self, app_view):
        app_view.hidden = True
        xts.export()
        app_data.current_ui = 'Menu'
        app_view.hidden = False