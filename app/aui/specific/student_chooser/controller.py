import ui
from app.aui.specific.student_chooser.view import View
from app.aui.specific.student_chooser.model import Model
from app.aui.generic.table_df.table_df_d import Delegate
from app.aui.generic.table_df_bar.table_df_bar_ds import TableDfBarDataSource
import app.data.app_data as app_data
import app.apputil.util as util

class Controller:
    def __init__(self, app_view):
        self.app_view = app_view
        if app_data.selected_group == None or app_data.selected_group == '':
            return
        source_path = util.get_group_folder() + app_data.selected_group + '.csv'
        model = Model(source_path)
        self.view = View(model, self)
        self.result = None
        table_size = (ui.get_screen_size()[0],int(ui.get_screen_size()[1] * 0.9))
        self.view.tv.delegate = Delegate(self)
        self.view.tv.data_source = TableDfBarDataSource(model, table_size)
        app_view.add_subview(self.view)
        self.view.wait_modal()
        app_data.selected_student = model.df['name'].loc[self.result]
        app_data.current_ui = 'Menu'
