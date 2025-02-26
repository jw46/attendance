from datetime import datetime
import os
from pathlib import Path
import app.apputil.config as config

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

def get_parent_path():
	path = Path(os.getcwd())
	return str(path.absolute())

def get_group_folder():
    return get_parent_path() + config.GROUP_FOLDER

def get_att_folder():
    return get_parent_path() + config.ATTENDANCE_FOLDER
    
def get_metadata_folder():
    return get_parent_path() + config.METADATA_FOLDER
    
def get_spreadsheet_folder():
    return get_parent_path() + config.SPREADSHEET_FOLDER
    
def get_classes_folder():
    return get_parent_path() + config.CLASSES_FOLDER

def get_documents_folder_path():
    return os.path.expanduser('~/Documents/')
