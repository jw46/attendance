from abc import ABC, abstractmethod

class AbstractDataSource (ABC):
    def __init__(self, model):
        self.model = model

    def tableview_number_of_sections(self, tableview):
        return 1

    def tableview_number_of_rows(self, tableview, section):
        return 1

    def tableview_cell_for_row(self, tableview, section, row):
        print('Abstract tableview_cell_for_row')
        pass

    def tableview_title_for_header(self, tableview, section):
        return 'Abstract'

    def tableview_can_delete(self, tableview, section, row):
        return True

    def tableview_can_move(self, tableview, section, row):
        return True

    def tableview_delete(self, tableview, section, row):
        pass

    def tableview_move_row(self, tableview, from_section, from_row, to_section, to_row):
        pass