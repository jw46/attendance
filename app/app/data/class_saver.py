import app.data.saver as saver
import app.data.app_data as app_data
import app.apputil.util as util

def save(df):
    return saver.save_df(df, util.get_classes_folder() + app_data.selected_group + '.csv')