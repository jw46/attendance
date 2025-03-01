import os
import sys
import pandas as pd
import numpy as np
import dialogs
import ui
import app.apputil.util as util
import app.data.loader as loader
import app.apputil.config as config


class ExportStudentAttendance:
    def __init__(self, app_data, pv):
        self.app_data = app_data
        self.pv = pv

    def get_att_files(self):
        att = os.listdir(util.get_att_folder())
        group_att = list(filter(lambda x: (x[20:-15], self.app_data.selected_group in x), att))
        return group_att
        
    def get_df(self, group_att):
        return loader.open_df(util.get_att_folder() + group_att)
    
    def filter_for_student(self, x):
        df = x[1]
        return (x[0], list(df.loc[df['name'] == self.app_data.selected_student, config.ATTENDANCE_COLUMN_NAME]))

    @ui.in_background
    def export(self):
        group_att = self.get_att_files()
        group_dfs = list(map(lambda x: (x, self.get_df(x)), group_att))
        group_dfs_dates = list(map(lambda x: (x[0][-14:-4], x[1]), group_dfs))
        student_attendance = list(map(lambda x: self.filter_for_student(x), group_dfs_dates))
        student_attendance_filtered = list(filter(lambda x: len(x[1]) != 0, student_attendance))
        sa_strings = list(map(lambda x: f'{x[0]} - {x[1][0]}', student_attendance_filtered))
        attendance_string = '\n'.join(sa_strings)
        title = f'Attendance for student {self.app_data.selected_student} for class {self.app_data.selected_group[20:-15]}\n'
        self.pv.hidden = True
        dialogs.share_text(title + attendance_string)
        print(title + attendance_string)
