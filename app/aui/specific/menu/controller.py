import ui
from app.aui.specific.menu.view import View
from app.aui.specific.menu.model import Model
from app.aui.generic.table_df.table_df_d import Delegate
from app.aui.generic.table_df_bar.table_df_bar_ds import TableDfBarDataSource
import app.data.app_data as app_data
import app.apputil.util as util

class Controller:
    def __init__(self, app_view):
        model = Model(util.get_menu_filepath())
        self.app_view = app_view
        self.view = View(model, self)
        self.view.tv.delegate = Delegate(self)
        self.result = None
        self.view.tv.data_source = TableDfBarDataSource(model, self.view.table_size)
        app_view.add_subview(self.view)
        self.view.wait_modal()
        app_data.current_ui = model.df['menu'].loc[self.result]
