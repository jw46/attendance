import os
import pandas as pd
import app.apputil.util as util
import app.data.loader as loader
import app.data.app_data as app_data
import app.apputil.config as config

def get_student_name(imie, imie2, nazwisko):
    if pd.notna(imie2):
        return f"{imie} {nazwisko}"
    return f"{imie} {imie2} {nazwisko}"


def load():
    if app_data.selected_group is None or app_data.selected_group == '':
        return None
    df = loader.open_df(util.get_group_folder() + app_data.selected_group + '.csv')
    df[config.STUDENT_NAME_COLUMN_NAME] = df.apply(lambda x: get_student_name(x['imie'], x['imie2'], x['nazwisko']), axis=1)
    if config.ATTENDANCE_COLUMN_NAME not in df:
        df[config.ATTENDANCE_COLUMN_NAME] = 'O'
    df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    return df
    
def load_one_student():
    if app_data.selected_student == None:
        return None
    df = load()
    df2 = df.query(f'name == {app_data.selected_student}')
    index = int(df2.index[0])
    df3 = df2.transpose()
    df3['field'] = df3.index
    df3['value'] = df3[index]
    df4 = df3[['field','value']]
    df4.reset_index(drop=True, inplace=True)
    return df4

def load_empty_student():
    data = {
        'field': ['nazwisko', 'imie', 'imie2', 'skreslony', 'rezygnacja', 'email', 'indeks', config.STUDENT_NAME_COLUMN_NAME, config.ATTENDANCE_COLUMN_NAME],
        'value': ['','','','','','','','','']
    }
    return pd.DataFrame(data)