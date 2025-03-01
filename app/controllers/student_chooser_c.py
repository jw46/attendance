import ui
from app.views.student_chooser_v import StudentChooserView
from app.models.student_chooser_m import StudentChooserModel
from app.views.student_chooser_d import StudentChooserDelegate
from app.views.table_df_ds import TableDfDataSource

class StudentChooserControler:
    def __init__(self):
        source_path = 'att/studenci_440-000-1S-JA-3_3_g304_2025-02-28.csv'
        model = StudentChooserModel(source_path)
        self.view = StudentChooserView(model)
        self.view.tv.delegate = StudentChooserDelegate(self)
        self.result = None
        table_size = (ui.get_screen_size()[0],int(ui.get_screen_size()[1] * 0.9))
        self.view.tv.width = table_size[0]
        self.view.tv.height = table_size[1]
        self.view.tv.data_source = TableDfDataSource(model, table_size)
        self.view.present('fullscreen')
        self.view.wait_modal()
        selected_student = model.df['name'].loc[self.result]
        print(selected_student)
