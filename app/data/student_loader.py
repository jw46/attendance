import os
import pandas as pd
import app.apputil.util as util
import app.data.loader as loader
import app.data.app_data as app_data
import app.apputil.config as config

def get_student_name(imie, imie2, nazwisko):
    if pd.notna(imie2):
        return f"{imie} {nazwisko}"
    return f"{imie} {imie2} {nazwisko}"


def load():
    if app_data.selected_group is None or app_data.selected_group == '':
        return None
    df = loader.open_df(util.get_group_folder() + app_data.selected_group + '.csv')
    if config.STUDENT_NAME_COLUMN_NAME not in df:
        df[config.STUDENT_NAME_COLUMN_NAME] = df.apply(lambda x: get_student_name(x['imie'], x['imie2'], x['nazwisko']), axis=1)
    if config.ATTENDANCE_COLUMN_NAME not in df:
        df[config.ATTENDANCE_COLUMN_NAME] = None
    return df
    

"""
Given the latest filename of a group from the groups folder, searches the attenace forlder for a file already saved today for the group
If any exist it returns a dataframe of the first from the list (there source never be more than one, but if there is it won't error)
If none exist it loads the filename provided fro mthe groups folder
"""
# def get_students(self, group_file_name):
#     att = os.listdir(util.get_att_folder())
#     group_att = list(filter(lambda x: x.startswith(group_file_name[0:-14]), att))
#     group_att_today = list(filter(lambda x: util.get_today() in x, group_att))
#     if len(group_att_today) == 0:
#         return loader.open_df(util.get_group_folder() + group_file_name)
#     return loader.open_df(util.get_att_folder() + group_att_today[0])
    