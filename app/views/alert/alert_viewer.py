import ui
from app.views.abstract_viewer import AbstractViewer
from app.views.alert.alert_data_source import AlertDataSource
import app.apputil.config as config

class AlertViewer(AbstractViewer):
    def __init__(self, parent_view, app_data):
        super().__init__(parent_view, app_data, has_close_button=True)
  
    def close_button_clicked(self, sender):
        self.app_data.current_ui = self.app_data.next_ui

    def show(self):
        tv_data_source = AlertDataSource(self.app_data)
        self.tv.data_source = tv_data_source
        self.tv.row_height = int(ui.get_screen_size()[1] * 0.7)
        super().show()
