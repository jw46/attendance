from abc import ABC, abstractmethod

class AbstractDelegate (ABC):
    def __init__(self, app_data, pv=None):
        self.app_data = app_data
        self.pv = pv

    def tableview_did_select(self, tableview, section, row):
        pass

    def tableview_did_deselect(self, tableview, section, row):
        pass

    def tableview_title_for_delete_button(self, tableview, section, row):
        return 'Delete'