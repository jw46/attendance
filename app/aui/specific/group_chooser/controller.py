import ui
from app.aui.specific.group_chooser.view import View
from app.aui.specific.group_chooser.model import Model
from app.aui.generic.table_df.table_df_d import Delegate
from app.aui.generic.table_df_bar.table_df_bar_ds import TableDfBarDataSource
import app.data.app_data as app_data

class Controller:
    def __init__(self):
        model = Model()
        self.view = View(model, self)
        self.view.tv.delegate = Delegate(self)
        self.result = None
        self.view.tv.data_source = TableDfBarDataSource(model, self.view.table_size)
        self.view.present('fullscreen')
        self.view.wait_modal()
        app_data.selected_group = model.df['Groups'].loc[self.result]
        app_data.selected_student = None
        app_data.current_ui = 'Menu'
