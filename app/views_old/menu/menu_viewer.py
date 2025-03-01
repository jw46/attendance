import ui
import app.views.abstract_viewer as abstract_viewer
from app.views.menu.menu_data_source import MenuDataSource
from app.views.menu.menu_delegate import MenuDelegate
from app.data.data_saver import DataSaver
import app.apputil.config as config

class MenuViewer(abstract_viewer.AbstractViewer):
    def __init__(self, parent_view, app_data):
        super().__init__(parent_view, app_data)

    def show(self):
        self.tv.row_height = 30
        self.tv.allows_selection = False
        tv_data_source = MenuDataSource(self.app_data)
        self.tv.data_source = tv_data_source
        tv_delegate = MenuDelegate(self.app_data)
        self.tv.delegate = tv_delegate
        self.tv.name = 'Main menu'
        self.tv.allows_selection = True
        self.tv.row_height = int(ui.get_screen_size()[1] * 0.7 / len(self.app_data.menu))
        super().show()
