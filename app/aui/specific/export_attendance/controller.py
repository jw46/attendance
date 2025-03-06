import time
import app.apputil.export_student_att as xsa
import app.data.app_data as app_data

class Controller:
    def __init__(self, app_view):
        app_view.hidden = True
        xsa.export()
        app_data.current_ui = 'Menu'
        app_view.hidden = False