import app.apputil.util as util

def save(df, filepath):
		df.to_csv(util.get_classes_folder() + filepath, sep=';', quotechar='"', index=False)