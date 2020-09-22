##############
# Automation for File Managment 
##############

# Author		: Jonas-Mika Senghaas 
# Date created	: 06.09.2020

import time
import os
import re
from datetime import datetime

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#Important Paths
downloads_folder = "/Users/jonassenghaas/Downloads"
desktop_folder = "/Users/jonassenghaas/Desktop"
folder_destination = "/Users/jonassenghaas/Library/Mobile Documents/com~apple~CloudDocs/Download_Center"

IDSP = "/Users/jonassenghaas/Library/Mobile Documents/com~apple~CloudDocs/ITU/A Studies/SI (Fall: Winter 2020)/Introduction to Data Science and Programming (15 ECTS)"
RBS = "/Users/jonassenghaas/Library/Mobile Documents/com~apple~CloudDocs/ITU/A Studies/SI (Fall: Winter 2020)/Data Science in Reseach, Business and Society (7.5 ECTS)"
MATH = "/Users/jonassenghaas/Library/Mobile Documents/com~apple~CloudDocs/ITU/A Studies/SI (Fall: Winter 2020)/Linear Algebra and Optimisation (7.5 ECTS)"

#Data Types
filetypes = {
"photo":[".jpeg", ".jpg", ".JPG" ".png", ".gif", ".icns", ".tiff", ".tif", ".HEIC"],
"video": [".mp4", ".mpg", ".mpeg", ".mov", ".wpd", ".MOV"],
"audio": [".mp3", ".wav", ".aif", ".mpa", ".mid", ".midi", ".cda"],
"productivity": [".doc", ".docx", ".odt", ".pdf", ".tex", ".wpd"],
"programming": [".py", ".java", ".js", ".php", ".bash", ".zsh", ".swift", ".c", ".cpp", ".cs"],
"datascience": [".txt", ".json", ".csv", ".dat", ".sql", ".xml"],
"creativity": [".psd", ".ai"],
"web":[".html"],
"installers":[".dmg", ".bin", ".zip", ".pkg"]
}

#testing 
#downloads_folder = "/Users/jonassenghaas/python/tryouts/file_manager/track_folder"
#desktop_folder = "/Users/jonassenghaas/python/tryouts/file_manager/track_folder2"
#folder_destination = "/Users/jonassenghaas/python/tryouts/file_manager/destination"

#formatting Filenames
def format_time():
	# create formatted time the when the file was moved 
	year, month, day = str(datetime.now()).split(" ")[0].split("-")
	formatted_time = "{}|{}|{}".format(year[2:], month, day)

	return formatted_time
def format_general(file):
	was_renamed = re.search("^\d\d\|\d\d\|\d\d", file)

	if was_renamed:
		formatted_name = file
	else: formatted_name = "{} {}".format(format_time(), file)

	return formatted_name
def format_itu(file):
	# extract file_name and path
	file_name, file_ext = os.path.splitext(file)
	was_renamed = re.search("^[A-Z]+\d+", file_name)

	if was_renamed:
		formatted_name = file 

	else:
		lecture, _type, name = "".join(file_name.split(" ")[1:]).split(",")[2:]
		formatted_name = "{} {}_{}{}".format(lecture.upper(), _type, name, file_ext)

	return formatted_name
def format_screenshot(file):
	formatted_name = file
	return formatted_name

def rename(file):
	match_itu = re.search("^itu", file)
	match_screen = re.search("^Screenshot", file)

	if match_itu:
		formatted_name = format_itu(file)
	elif match_screen:
		formatted_name = format_screenshot(file)
	else: formatted_name = format_general(file)

	return formatted_name

#Sorting depending on File
def sort_datatype(path, file):
	i = 1
	source_path = "{}/{}".format(path, file)
	file_name, file_ext = os.path.splitext(file)

	if file_ext in filetypes["video"]:
		try: 
			os.mkdir("{}/video".format(folder_destination)) 
		except: None
		
		new_path = "{}/video/{}".format(folder_destination, file)
		os.rename(source_path, new_path)
		print(">>> moved to <videos>")

	#photos
	elif file_ext in filetypes["photo"]:
		try:
			os.mkdir("{}/photos".format(folder_destination))
		except: None

		new_path = "{}/photos/{}".format(folder_destination, file)
		os.rename(source_path, new_path)
		print(">>> moved to <photos>")

	#audio
	elif file_ext in filetypes["audio"]:
		try:
			os.mkdir("{}/audio".format(folder_destination))
		except: None

		new_path = "{}/audio/{}".format(folder_destination, file)
		os.rename(source_path, new_path)
		print(">>> moved to <audio>")

	#creativity
	elif file_ext in filetypes["creativity"]:
		try:
			os.mkdir("{}/creativity".format(folder_destination)) 
		except: None
		new_path = "{}/creativity/{}".format(folder_destination, file)
		os.rename(source_path, new_path)
		print(">>> moved to <creativity>")

	#productivity
	elif file_ext in filetypes["productivity"]:
		try:
			os.mkdir("{}/productivity".format(folder_destination)) 
		except: None
		new_path = "{}/productivity/{}".format(folder_destination, file)
		os.rename(source_path, new_path)
		print(">>> moved to <productivity>")

	#programming
	elif file_ext in filetypes["programming"]:
		try:
			os.mkdir("{}/programming".format(folder_destination)) 
		except: None
		new_path = "{}/programming/{}".format(folder_destination, file)
		os.rename(source_path, new_path)
		print(">>> moved to <programming>")

	#installers
	elif file_ext in filetypes["installers"]:
		try:
			os.mkdir("{}/installer".format(folder_destination)) 
		except: None
		new_path = "{}/installer/{}".format(folder_destination, file)
		os.rename(source_path, new_path)
		print(">>> moved to <installer>")

	#data_analysis
	elif file_ext in filetypes["datascience"]:
		try:
			os.mkdir("{}/data_analysis".format(folder_destination)) 
		except: None
		new_path = "{}/data_analysis/{}".format(folder_destination, file)
		os.rename(source_path, new_path)
		print(">>> moved to <data_analysis>")

	#web
	elif file_ext in filetypes["web"]:
		try:
			os.mkdir("{}/web".format(folder_destination)) 
		except: None
		new_path = "{}/web/{}".format(folder_destination, file)
		os.rename(source_path, new_path)
		print(">>> moved to <web>")

	else:
		try:
			os.mkdir("{}/other".format(folder_destination)) 
		except: None
		new_path = "{}/other/{}".format(folder_destination, file)
		os.rename(source_path, new_path)
		print(">>> moved to <other>")

	#renaming file
	new_name = rename(file)
	name, ext = os.path.splitext(new_name)
	root = "/".join(new_path.split("/")[:-1])
	
	renamed_path = "{}/{}".format(root, new_name)
	
	#check for duplicates
	file_exists = os.path.exists(renamed_path)
	
	while file_exists:
		i += 1
		renamed_path = root + "/" + name + str(i) + ext
		file_exists = os.path.exists(renamed_path)
		
	os.rename(new_path, renamed_path)
def sort_itu(path,file):
	i = 1
	source_path = "{}/{}".format(path, file)
	file_name, file_ext = os.path.splitext(file)

	course, week = "".join(file_name.split(" ")[1:]).split(",")[0:2]
	
	if course == str(1):
		try:
			os.mkdir("{}/Week {}".format(IDSP, week))
		except: None
		new_path = "{}/Week {}/{}".format(IDSP, week, file)
		os.rename(source_path, new_path)
		print(">>> succesfully moved to IDSP")

	elif course == str(2):
		try:
			os.mkdir("{}/Week {}".format(MATH, week))
		except: None
		new_path = "{}/Week {}/{}".format(MATH, week, file)
		os.rename(source_path, new_path)
		print(">>> succesfully moved to Linear Algebra and Optimisation")

	elif course == str(3):
		try:
			os.mkdir("{}/Week {}".format(RBS, week))
		except: None
		new_path = "{}/Week {}/{}".format(RBS, week, file)
		os.rename(source_path, new_path)
		print(">>> succesfully moved to RBS")

	else: print("Something went wrong")

	#renaming file
	new_name = rename(file)
	print(new_name)
	root = "/".join(new_path.split("/")[:-1])
	
	renamed_path = "{}/{}".format(root, new_name)
	print(renamed_path)
		
	os.rename(new_path, renamed_path)
def sort_screenshot(path,file):
	i = 1
	source_path = "{}/{}".format(path, file)

	try: 
		os.mkdir("{}/screenshots".format(folder_destination)) 
	except: None
			
	new_path = "{}/screenshots/{}".format(folder_destination, file)
	os.rename(source_path, new_path)
	print(">>> moved to <screenshots>")

#Driver Code, when watchdogs recognizes change in tracked folders
def on_modified(event):
	for file in os.listdir(event.src_path):
		try:
			match_itu = re.search("^itu", file)
			match_screen = re.search("^Screenshot", file)

			if match_itu:
				sort_itu(event.src_path, file)
			elif match_screen:
				sort_screenshot(event.src_path, file)
			else: 
				sort_datatype(event.src_path, file)

			#print("A change to {} has been detected".format(event.src_path.split("/")[-1].upper()))
		except: None 

def main():
	#initialize event handler as instance of class "FileSystemEventHandler"
	event_handler = FileSystemEventHandler()
	event_handler.on_modified = on_modified

	#initialize and start observer of downloads folder
	downloads_observer = Observer()
	downloads_observer.schedule(event_handler, downloads_folder, recursive=False)
	downloads_observer.start()

	#initialize and start observer of desktop folder
	desktop_observer = Observer()
	desktop_observer.schedule(event_handler, desktop_folder, recursive=False)
	desktop_observer.start()
	
	#stop both observers with keyboard interrupt
	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
			downloads_observer.stop()
			desktop_observer.stop()
	downloads_observer.join()
	desktop_observer.join()

if __name__ == "__main__":
	print("Running...")
	main()
	