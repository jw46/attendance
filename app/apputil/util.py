from datetime import datetime
import os
from pathlib import Path
import app.apputil.config as config
import app.data.app_data as app_data

"""
Returns today's date in the format in the filenames
"""
def get_today():
    return datetime.now().strftime("%Y-%m-%d")

"""
Not needed because string ordering will work fine
"""
def string_to_date(s):
    f = "%Y-%m-%d"
    return datetime.strptime(s, f)

def date_to_string(d):
    f = "%Y-%m-%d"
    return d.strftime(f)

def get_app_path():
    path = Path(os.getcwd())
    return str(path.absolute())

def get_group_folder():
    return get_app_path() + config.GROUP_FOLDER

def get_att_folder():
    return get_app_path() + config.ATTENDANCE_FOLDER

def get_metadata_folder():
    return get_app_path() + config.METADATA_FOLDER

def get_spreadsheet_folder():
    return get_app_path() + config.SPREADSHEET_FOLDER

def get_classes_folder():
    return get_app_path() + config.CLASSES_FOLDER

def get_temp_folder():
    return get_app_path() + config.TEMP_FOLDER

def get_documents_folder_path():
    return os.path.expanduser('~/Documents/')

def get_menu_filepath():
    return get_app_path() + '/metadata/menu.csv'

def get_bar_text():
    if app_data.selected_group is None:
        return app_data.selected_date
    if app_data.selected_student is None:
        return app_data.selected_group + '   ' + app_data.selected_date
    return app_data.selected_group + '   ' + app_data.selected_date + '   ' + app_data.selected_student