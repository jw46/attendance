import time
import app.apputil.backup_data as bd
import app.data.app_data as app_data

class Controller:
    def __init__(self, app_view):
        app_view.hidden = True
        bd.save()
        app_data.current_ui = 'Menu'
        app_view.hidden = False