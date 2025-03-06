import os
from zipfile import ZipFile 
from pathlib import Path
import dialogs
import app.apputil.util as util


def get_filepath():
    filepath = util.get_temp_folder() + 'backup' + util.get_timestamp() + '.zip'
    return filepath

def get_file_list():
    app_folder = util.get_app_path()
    l = list(os.walk(app_folder))
    l = list(filter(lambda x: '.git' not in x[0], l))
    l = list(filter(lambda x: '/app' not in x[0], l))
    l = list(filter(lambda x: '__pycache__' not in x[0], l))
    l = list(filter(lambda x: 'metadata' not in x[0], l))
    l = list(filter(lambda x: 'temp' not in x[0], l))
    l = list(filter(lambda x: x[0] != app_folder, l))
    lol = list(map(lambda x: list(map(lambda y: x[0] + '/' + y, x[2])), l))
    flat = [item for sublist in lol for item in sublist]
    flat_t = list(map(lambda x: (x, x.replace(app_folder, '')), flat))
    return flat_t

def share_file(filepath):
	dialogs.share_url(Path(filepath).absolute().resolve().as_uri())

def save():
    file_list = get_file_list()
    output_filepath = get_filepath()
    with ZipFile(output_filepath, mode="w") as archive:
        for file_path in file_list:
            archive.write(file_path[0], arcname=file_path[1])
    share_file(output_filepath)
    util.clean_temp()






