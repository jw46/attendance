import os
import pandas as pd
import app.apputil.util as util
import app.apputil.config as config
import app.data.loader as loader

"""
Loads the csv file for a group or reloads today's attendance for the group
"""
class DataLoader:

    """
    Gets all of the CSV files that have the same group name
    """
    def get_matching_files(self, group_name, data):
        return list(filter(lambda x: x.startswith(group_name), data))

    """
        From a group of files, returns the most recent date from the file name
    """
    def get_latest(self, data):
        just_dates = list(map(lambda x: x[-14:-4], data))
        return max(just_dates)

    """
    Gets the most recently dated file for a group.
    Means that if the group changes you can add a new file from SOJO without the need to delete old files.
    """
    def get_one_file_per_group(self, data):
        group_names = set(map(lambda x: x[0:-14], data))
        grouped_group_files = list(map(lambda x: (x, self.get_matching_files(x, data)), group_names))
        groups_latest = list(map(lambda x: x[0] + self.get_latest(x[1]) + '.csv', grouped_group_files))
        return groups_latest

    """
    Gets a list of the files in the groups folder
    """
    def load_groups(self):
        data = os.listdir(util.get_group_folder())
        groups = self.get_one_file_per_group(data)
        sorted = groups.sort()
        return groups

    """
    Given the latest filename of a group from the groups folder, searches the attenace forlder for a file already saved today for the group
    If any exist it returns a dataframe of the first from the list (there source never be more than one, but if there is it won't error)
    If none exist it loads the filename provided fro mthe groups folder
    """
    def get_students(self, group_file_name):
        att = os.listdir(util.get_att_folder())
        group_att = list(filter(lambda x: x.startswith(group_file_name[0:-14]), att))
        group_att_today = list(filter(lambda x: util.get_today() in x, group_att))
        if len(group_att_today) == 0:
            df = loader.open_df(util.get_group_folder() + group_file_name)
        else:
            df = loader.open_df(util.get_att_folder() + group_att_today[0])
        return df.sort_values(['nazwisko', 'imie', 'imie2'], ascending=True)
    
