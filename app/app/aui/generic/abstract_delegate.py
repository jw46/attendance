from abc import ABC, abstractmethod

class AbstractDelegate (ABC):
    def __init__(self, controller=None):
        self.controller = controller

    def tableview_did_select(self, tableview, section, row):
        pass

    def tableview_did_deselect(self, tableview, section, row):
        pass

    def tableview_title_for_delete_button(self, tableview, section, row):
        return 'Delete'