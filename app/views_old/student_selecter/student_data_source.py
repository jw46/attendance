import ui_old
import sys
import traceback
import pandas as pd
import app.views.student_selecter.options_view as options_view
import app.apputil.config as config

"""
 See 
"""
class StudentDataSource (object):
    def __init__(self, app_data):
        self.app_data = app_data
        pd.set_option('display.max_columns', None)

    def tableview_number_of_sections(self, tableview):
        # Return the number of sections (defaults to 1)
        return 1

    def tableview_number_of_rows(self, tableview, section):
        # Return the number of rows in the section
        return len(self.app_data.students_df.index) -1

    """
    Get the index in list AppData.sc_object from the value matching the class ui.SegmentedControl object passed from the SegmentedControl.action
    The gets which button is selected, looking the the value in config.options
    and writes to the the same index in AppData.attendence_list
    """
    def record_selection(self, sc):
        i = self.app_data.sc_object.index(sc)
        self.app_data.students_df.iloc[i, 7] = config.OPTIONS[sc.selected_index]

    def get_sc(self, row):
        ov = options_view.OptionsView()
        sc = ov.get_sc()
        sc.action = self.record_selection
        self.app_data.sc_object[row] = sc
        if config.ATTENDANCE_COLUMN_NAME in self.app_data.students_df and pd.notna(self.app_data.students_df[config.ATTENDANCE_COLUMN_NAME][row]):
            sc.selected_index = config.OPTIONS.index(self.app_data.students_df[config.ATTENDANCE_COLUMN_NAME][row])   
        else:
            sc.selected_index = -1     
        return sc

    def get_student_name(self, row):
        if pd.notna(self.app_data.students_df['imie2'][row]):
            return f"{self.app_data.students_df['imie'][row]} {self.app_data.students_df['nazwisko'][row]}"
        return f"{self.app_data.students_df['imie'][row]} {self.app_data.students_df['imie2'][row]} {self.app_data.students_df['nazwisko'][row]}"

    """
    Creates a TableViewCell containing a SegmentedControl on the left side and a Label on the right side contatining the student's name
    When the use click on the button in the SegmentedControl record_selection is called to save the selection
    """
    def tableview_cell_for_row(self, tableview, section, row):
        cell = ui_old.TableViewCell()
        cell.bounds = (0, 0, tableview.width, tableview.row_height)
        student_name = self.get_student_name(row)
        sc = self.get_sc(row)
        cell.content_view.add_subview(sc)
        name_label = ui_old.Label()
        name_label.border_width = 0.5
        name_label.text = student_name
        name_label.frame = (sc.width, 0, tableview.width  - sc.width, tableview.row_height)
        name_label.alignment = ui_old.ALIGN_LEFT
        cell.content_view.add_subview(name_label)
        return cell

    def tableview_title_for_header(self, tableview, section):
        # Return a title for the given section.
        # If this is not implemented, no section headers will be shown.
        return 'students'

    def tableview_can_delete(self, tableview, section, row):
        # Return True if the user should be able to delete the given row.
        return True

    def tableview_can_move(self, tableview, section, row):
        # Return True if a reordering control should be shown for the given row (in editing mode).
        return True

    def tableview_delete(self, tableview, section, row):
        # Called when the user confirms deletion of the given row.
        pass

    def tableview_move_row(self, tableview, from_section, from_row, to_section, to_row):
        # Called when the user moves a row with the reordering control (in editing mode).
        pass
