import os
import pandas as pd
import app.apputil.util as util
import app.apputil.config as config
import app.data.loader as loader
import app.data.app_data as app_data

"""
Loads the csv file for a group or reloads today's attendance for the group
"""

"""
Gets all of the CSV files that have the same group name
"""
def get_matching_files(group_name, data):
    return list(filter(lambda x: x.startswith(group_name), data))

"""
    From a group of files, returns the most recent date from the file name
"""
def get_latest(data):
    just_dates = list(map(lambda x: x[-14:-4], data))
    return max(just_dates)

"""
Gets the most recently dated file for a group.
Means that if the group changes you can add a new file from SOJO without the need to delete old files.
"""
def get_one_file_per_group(data):
    group_names = set(map(lambda x: x[0:-14], data))
    grouped_group_files = list(map(lambda x: (x, get_matching_files(x, data)), group_names))
    groups_latest = list(map(lambda x: x[0] + get_latest(x[1]) + '.csv', grouped_group_files))
    return groups_latest

"""
Gets a list of the files in the groups folder
"""
def load_groups():
    data = os.listdir(util.get_group_folder())
    return get_one_file_per_group(data)

def get_group_names():
    if len(app_data.group_list) < 0:
        return app_data.group_list
    data = os.listdir(util.get_group_folder())
    filtered_data = list(filter(lambda x: x.endswith('.csv'), data))
    reduced_names = list(map(lambda x: x[:-4], filtered_data))
    app_data.group_list = reduced_names
    return pd.DataFrame(reduced_names, columns=['Groups'])

    
