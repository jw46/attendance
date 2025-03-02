import os
import app.data.loader as loader
import app.data.app_data as app_data
import app.apputil.util as util
import app.data.student_loader as sl

def load():
    att_file = util.get_att_folder() + app_data.selected_group + app_data.selected_date + '.csv'
    if os.path.isfile(att_file):
        return loader.open_df(att_file)
    return sl.load()