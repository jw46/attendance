import os
import shutil


def get_parent_path():
	path = Path(os.getcwd())
	return str(path.parent.parent.absolute())
source = get_parent_path()   
destination = '/private/var/mobile/Containers/Data/Application/EC803869-F9F4-4BC3-8182-AEF407918EFA/Documents'
print(os.listdir(destination))
#source = 
shutil.copytree(source, destination, dirs_exist_ok=True)
#print('The app should now be updated')

#print(os.path.expandvars("~"))
