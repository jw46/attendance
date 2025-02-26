import app.data.loader as loader

def load(app_data):
    app_data.class_df = loader.open_df(app_data.selected_group)