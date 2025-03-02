import pandas as pd
import app.apputil.config as config
import app.data.app_data as app_data
import app.data.class_loader as cl
import app.data.app_data as app_data

class Model():
    def __init__(self):
        self.df = cl.load()
        self.column_widgets = [('Class Dates', 'label')]
        self.visible_columns = list(map(lambda x: x[0], self.column_widgets))
        self.button_text = config.STANDARD_BUTON_TEXT
        self.label_text = app_data.selected_group
        self.table_name = 'Choose Class Date'
