import ui
from app.aui.specific.change_date.view import View
from app.aui.specific.change_date.model import Model
from app.aui.generic.table_df.table_df_d import Delegate
from app.aui.generic.table_df_bar.table_df_bar_ds import TableDfBarDataSource
import app.data.app_data as app_data

class Controller:
    def __init__(self, app_view):
        model = Model()
        self.app_view = app_view
        self.view = View(model, self)
        self.view.tv.delegate = Delegate(self)
        self.result = None
        self.view.tv.data_source = TableDfBarDataSource(model, self.view.table_size)
        app_view.add_subview(self.view)
        self.view.wait_modal()
        app_data.selected_date = model.df['Class Dates'].loc[self.result]
        app_data.current_ui = 'Menu'
