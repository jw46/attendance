import os
import pandas as pd
import app.apputil.util as util
import app.apputil.config as config

class DataSaver:

	def filename_to_today(self, fn):
		return fn[0:-14] + util.get_today() + '.csv'

	def save(self, df, filepath):
		df.to_csv(filepath, sep=';', quotechar='"', index=False)

	def save_attendence(self, df, group_filename):
		self.save(df, util.get_att_folder() + self.filename_to_today(group_filename))
