import os
import dialogs
import app.data.app_data as app_data
import app.apputil.util as util
import app.apputil.config as config
import app.data.loader as loader



def get_att_files():
	att_files = os.listdir(util.get_att_folder())
	att_files = list(filter(lambda x: x.startswith(app_data.selected_group), att_files))
	return att_files

def load(filename):
	return (filename[3:-4], loader.open_df(util.get_att_folder() + filename))

def get_att(x):
	result_df = x[1].query(f'{config.STUDENT_NAME_COLUMN_NAME} == "{app_data.selected_student}"')
	if len(result_df) > 0:
		att = result_df['attendance'].values[0]
	return x[0] + ' - ' + att

def share_sreadsheet(s):
	dialogs.share_text(s)

def export():
	if app_data.selected_student is None:
		return
	att_files = get_att_files()
	att_dfs = list(map(lambda x: load(x), att_files))
	att_string = list(map(lambda x: get_att(x), att_dfs))
	output = f"Attendance of {app_data.selected_student}in group {app_data.selected_group}\n" + '\n'.join(att_string)
	share_sreadsheet(output)
	
