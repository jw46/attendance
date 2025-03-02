import ui
from app.aui.specific.record_class_title.view import View
from app.aui.specific.record_class_title.model import Model
# from app.aui.specific.record_class_title.delegate import Delegate
from app.aui.specific.record_class_title.data_source import DataSource
import app.data.app_data as app_data
import app.data.class_saver as cs

class Controller:
    def __init__(self, app_view):
        self.app_view = app_view
        model = Model()
        self.view = View(model, self)
        # self.view.tv.delegate = Delegate(self)
        self.result = None
        self.view.tv.data_source = DataSource(model, self.view.table_size)
        app_view.add_subview(self.view)
        self.view.wait_modal()
        cs.save(model.df)
        app_data.current_ui = 'Menu'
