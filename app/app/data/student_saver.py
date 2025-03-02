import app.data.saver as saver
import app.data.app_data as app_data
import app.apputil.util as util
import app.data.student_loader as loader

def add_and_save(df):
    students = loader.load()
    print(students)
    print(df['value'].to_list())
    students.loc[len(students)] = df['value'].to_list()
    saver.save_df(students, util.get_group_folder() + app_data.selected_group + '.csv')