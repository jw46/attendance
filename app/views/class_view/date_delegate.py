from app.views.abstract_delegate import AbstractDelegate

class DateDelegate (AbstractDelegate):
    def __init__(self, app_data, is_class_editor):
        super().__init__(app_data)
        self.is_class_editor = is_class_editor

    def tableview_did_select(self, tableview, section, row):
        if self.is_class_editor:
            pass
        else:
            self.app_data.selected_date = self.app_data.class_df['Class Dates'][row]
            self.app_data.current_ui = 'Menu'
            tableview.close()
