from app.aui.generic.abstract_delegate import AbstractDelegate


class Delegate(AbstractDelegate):
    def __init__(self, controller):
        super().__init__(controller)


    def tableview_did_select(self, tableview, section, row):
        self.controller.result = row
        self.controller.view.close()