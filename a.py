import os
from pathlib import Path
import pandas as pd
#print(os.getcwd())

def get_parent_path():
	path = Path(os.getcwd())
	return str(path.absolute())

filepath = get_parent_path() + '/metadata'
print(os.listdir(filepath))
# df = pd.read_csv(filepath, sep=';', quotechar='"')
# print(df)
