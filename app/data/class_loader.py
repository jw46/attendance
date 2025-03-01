import app.data.loader as loader
import app.apputil.util as util
class ClassLoader:
	def load(self, app_data):
		df = loader.open_df(util.get_classes_folder() + app_data.selected_group)
		app_data.class_df = df.sort_values('Class Dates', ascending=True)