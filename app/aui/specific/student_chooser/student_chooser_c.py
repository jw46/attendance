import ui
from app.aui.specific.student_chooser.student_chooser_v import StudentChooserView
from app.aui.specific.student_chooser.student_chooser_m import StudentChooserModel
from app.aui.specific.student_chooser.student_chooser_d import StudentChooserDelegate
from app.aui.generic.table_df_bar.table_df_bar_ds import TableDfBarDataSource

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
        self.view.tv.data_source = TableDfBarDataSource(model, table_size)
        self.view.present('fullscreen')
        self.view.wait_modal()
        selected_student = model.df['name'].loc[self.result]
        print(selected_student)
