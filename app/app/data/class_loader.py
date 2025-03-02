import app.data.loader as loader
import app.data.app_data as app_data
import app.apputil.util as util

def load():
    return loader.open_df(util.get_classes_folder() + app_data.selected_group + '.csv')