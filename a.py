import os
from pathlib import Path
#print(os.getcwd())

def get_parent_path():
	path = Path(os.getcwd())
	return str(path.absolute())

c = get_parent_path()
print(c)
