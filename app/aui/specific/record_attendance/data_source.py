import ui
from app.aui.generic.table_df_bar.table_df_bar_ds import TableDfBarDataSource
from app.aui.specific.record_attendance.options_view import OptionsView
import app.apputil.config as config


class DataSource(TableDfBarDataSource):
    def __init__(self, model, table_size):
        super().__init__(model, (int(table_size[0] - 300), table_size[1] - 75))
        self.sc_object = [None for i in range(len(self.model.df.index))]


    def record_selection(self, sender):
        row = self.sc_object.index(sender)
        self.model.df[config.ATTENDANCE_COLUMN_NAME].loc[row] = config.OPTIONS[sender.selected_index]

    def get_sc(self, row):
        ov = OptionsView()
        sc = ov.get_sc()
        sc.action = self.record_selection
        print(len(self.model.df.index))
        self.sc_object[row] = sc
        select_value = self.model.df[config.ATTENDANCE_COLUMN_NAME][row]
        if select_value:
            sc.selected_index = config.OPTIONS.index(select_value)
        ov.x = 0
        ov.y = 0
        ov.width = 300
        ov.height = 50
        return sc

    def tableview_cell_for_row(self, tableview, section, row):
        cell = ui.TableViewCell()
        ov = self.get_sc(row)
        cell.add_subview(ov)
        cell.bounds = (0, 0, self.table_size[0], 50)
        self.add_widgets(cell, row)
        return cell