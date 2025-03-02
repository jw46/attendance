import ui
from app.aui.specific.record_attendance.view import View
from app.aui.specific.record_attendance.model import Model
from app.aui.generic.table_df.table_df_d import Delegate
from app.aui.specific.record_attendance.data_source import DataSource
import app.data.app_data as app_data
import app.apputil.util as util
import app.data.att_saver as att_saver

class Controller:
    def __init__(self, app_view):
        self.app_view = app_view
        if app_data.selected_group == None or app_data.selected_group == '':
            return
        source_path = util.get_group_folder() + app_data.selected_group + '.csv'
        model = Model(source_path)
        self.view = View(model, self)
        table_size = (ui.get_screen_size()[0],int(ui.get_screen_size()[1] * 0.9))
        self.view.tv.delegate = Delegate(self)
        self.view.tv.width = table_size[0]
        self.view.tv.height = table_size[1]
        self.view.tv.data_source = DataSource(model, table_size)
        app_view.add_subview(self.view)
        self.view.wait_modal()
        att_saver.save(model.df)
        app_data.current_ui = 'Menu'
