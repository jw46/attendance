import ui
from app.aui.specific.add_student.view import View
from app.aui.specific.add_student.model import Model
from app.aui.generic.table_df.table_df_d import Delegate
from app.aui.specific.add_student.data_source import DataSource
import app.data.app_data as app_data
import app.data.student_saver as ss

class Controller:
    def __init__(self, app_view):
        model = Model()
        self.app_view = app_view
        self.view = View(model, self)
        self.view.tv.delegate = Delegate(self)
        self.result = None
        self.view.tv.data_source = DataSource(model, self.view.table_size)
        app_view.add_subview(self.view)
        self.view.wait_modal()
        ss.add_and_save(model.df)
        app_data.current_ui = 'Menu'


