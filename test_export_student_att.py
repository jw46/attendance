import pytest
import app.apputil.export_student_att as xsa
import app.data.app_data as app_data

def test_get_att():
    app_data.selected_group = '104'
    app_data.selected_student = 'Piotr Maź'
    files = xsa.get_att_files()
    file = files[0]
    df = xsa.load(file)
    s = xsa.get_att(df)
    print(s)

def test_export():
    s = xsa.export()
    print(s)