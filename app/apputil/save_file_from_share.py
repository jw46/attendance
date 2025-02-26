# coding: utf-8

import appex
import console
import re

"""
Playing with downloading csv files from browser and using the iOS share to execute this script to copy the files into the groups folder.
"""
def main():
	if not appex.is_running_extension():
		print('This script is intended to be run from the sharing extension.')
		return
	fp = appex.get_file_path()
	print(fp)



if __name__ == '__main__':
	main()
	
