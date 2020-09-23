##############
# Automation for File Managment 
##############

# Author		: Jonas-Mika Senghaas 
# Date created	: 06.09.2020

from re import match
import time
import os
import re
import pwd
import json

from watchdog.observers.api import ObservedWatch
from helpers import *
from strategies import *
from datetime import datetime

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Config
with open('./sorting.json', 'r') as f:
	CONFIG = json.load(f)

#Sorting depending on File
# def sort_datatype(path, file):
# 	i = 1
# 	source_path = "{}/{}".format(path, file)
# 	file_name, file_ext = os.path.splitext(file)

# 	if file_ext in filetypes["video"]:
# 		try: 
# 			os.mkdir("{}/video".format(folder_destination)) 
# 		except: None
		
# 		new_path = "{}/video/{}".format(folder_destination, file)
# 		os.rename(source_path, new_path)
# 		print(">>> moved to <videos>")

# 	#photos
# 	elif file_ext in filetypes["photo"]:
# 		try:
# 			os.mkdir("{}/photos".format(folder_destination))
# 		except: None

# 		new_path = "{}/photos/{}".format(folder_destination, file)
# 		os.rename(source_path, new_path)
# 		print(">>> moved to <photos>")

# 	#audio
# 	elif file_ext in filetypes["audio"]:
# 		try:
# 			os.mkdir("{}/audio".format(folder_destination))
# 		except: None

# 		new_path = "{}/audio/{}".format(folder_destination, file)
# 		os.rename(source_path, new_path)
# 		print(">>> moved to <audio>")

# 	#creativity
# 	elif file_ext in filetypes["creativity"]:
# 		try:
# 			os.mkdir("{}/creativity".format(folder_destination)) 
# 		except: None
# 		new_path = "{}/creativity/{}".format(folder_destination, file)
# 		os.rename(source_path, new_path)
# 		print(">>> moved to <creativity>")

# 	#productivity
# 	elif file_ext in filetypes["productivity"]:
# 		try:
# 			os.mkdir("{}/productivity".format(folder_destination)) 
# 		except: None
# 		new_path = "{}/productivity/{}".format(folder_destination, file)
# 		os.rename(source_path, new_path)
# 		print(">>> moved to <productivity>")

# 	#programming
# 	elif file_ext in filetypes["programming"]:
# 		try:
# 			os.mkdir("{}/programming".format(folder_destination)) 
# 		except: None
# 		new_path = "{}/programming/{}".format(folder_destination, file)
# 		os.rename(source_path, new_path)
# 		print(">>> moved to <programming>")

# 	#installers
# 	elif file_ext in filetypes["installers"]:
# 		try:
# 			os.mkdir("{}/installer".format(folder_destination)) 
# 		except: None
# 		new_path = "{}/installer/{}".format(folder_destination, file)
# 		os.rename(source_path, new_path)
# 		print(">>> moved to <installer>")

# 	#data_analysis
# 	elif file_ext in filetypes["datascience"]:
# 		try:
# 			os.mkdir("{}/data_analysis".format(folder_destination)) 
# 		except: None
# 		new_path = "{}/data_analysis/{}".format(folder_destination, file)
# 		os.rename(source_path, new_path)
# 		print(">>> moved to <data_analysis>")

# 	#web
# 	elif file_ext in filetypes["web"]:
# 		try:
# 			os.mkdir("{}/web".format(folder_destination)) 
# 		except: None
# 		new_path = "{}/web/{}".format(folder_destination, file)
# 		os.rename(source_path, new_path)
# 		print(">>> moved to <web>")

# 	else:
# 		try:
# 			os.mkdir("{}/other".format(folder_destination)) 
# 		except: None
# 		new_path = "{}/other/{}".format(folder_destination, file)
# 		os.rename(source_path, new_path)
# 		print(">>> moved to <other>")

# 	#renaming file
# 	new_name = rename(file)
# 	name, ext = os.path.splitext(new_name)
# 	root = "/".join(new_path.split("/")[:-1])
	
# 	renamed_path = "{}/{}".format(root, new_name)
	
# 	#check for duplicates
# 	file_exists = os.path.exists(renamed_path)
	
# 	while file_exists:
# 		i += 1
# 		renamed_path = root + "/" + name + str(i) + ext
# 		file_exists = os.path.exists(renamed_path)
		
# 	os.rename(new_path, renamed_path)

# def sort_itu(path,file):
# 	i = 1
# 	source_path = "{}/{}".format(path, file)
# 	file_name, file_ext = os.path.splitext(file)

# 	course, week = "".join(file_name.split(" ")[1:]).split(",")[0:2]
	
# 	if course == str(1):
# 		try:
# 			os.mkdir("{}/Week {}".format(IDSP, week))
# 		except: None
# 		new_path = "{}/Week {}/{}".format(IDSP, week, file)
# 		os.rename(source_path, new_path)
# 		print(">>> succesfully moved to IDSP")

# 	elif course == str(2):
# 		try:
# 			os.mkdir("{}/Week {}".format(MATH, week))
# 		except: None
# 		new_path = "{}/Week {}/{}".format(MATH, week, file)
# 		os.rename(source_path, new_path)
# 		print(">>> succesfully moved to Linear Algebra and Optimisation")

# 	elif course == str(3):
# 		try:
# 			os.mkdir("{}/Week {}".format(RBS, week))
# 		except: None
# 		new_path = "{}/Week {}/{}".format(RBS, week, file)
# 		os.rename(source_path, new_path)
# 		print(">>> succesfully moved to RBS")

# 	else: print("Something went wrong")

# 	#renaming file
# 	new_name = rename(file)
# 	print(new_name)
# 	root = "/".join(new_path.split("/")[:-1])
	
# 	renamed_path = "{}/{}".format(root, new_name)
# 	print(renamed_path)
		
# 	os.rename(new_path, renamed_path)

def move_file(src, file, dest):
	try: os.makedirs(f'{dest}')
	except: None

	os.rename(f'{src}/{file}', f'{dest}/{file}')
	print(f">>> moved {file} to <{dest}>")

#Driver Code, when watchdogs recognizes change in tracked folders
def on_modified(event):
	# Rule of thumb, don't put functions in loop signature, it can make it significant more slot.
	# I don't think it makes a big impact here, but it will in other languages.

	try:
		file_names = os.listdir(event.src_path)
	except:
		return

	for file in file_names:
		# items() return the key/name and value of a dictionary
		for match, dest in CONFIG['match'].items():
			dest_filtered = filter_variables(dest, CONFIG['paths'])

			try:
				if re.match(match, file):
					move_file(event.src_path, file, dest_filtered)
			except: None

		# src = f'{event.src_path}/{file}'

		# if re.match("^itu", file):
		# 	# sort_itu(src, CONFIG[])
		# 	pass
		# elif re.match("^Screenshot", file):
		# 	sort_screenshot(src, CONFIG['img_dest'])
		# else:
		# 	sort_datatype(event.src_path, file)

def main():
	#initialize event handler as instance of class "FileSystemEventHandler"
	observers = {}

	event_handler = FileSystemEventHandler()
	# event_handler.on_modified = on_modified
	event_handler.on_modified = on_modified

	for ob_path in CONFIG['watch']:
		obs = Observer()

		ob_path_filtered = filter_variables(ob_path, CONFIG['paths'])

		obs.schedule(event_handler, ob_path_filtered, recursive=False)
		obs.start()

		observers[ob_path_filtered] = obs

	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		for obs in observers.values():
			obs.stop()

	for obs in observers.values():
		obs.join()

if __name__ == "__main__":
	print("Running...")
	main()