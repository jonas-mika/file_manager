import os
import time
import re
from datetime import datetime

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

downloads_folder = "/Users/jonassenghaas/python/tryouts/file_manager/track_folder"
desktop_folder = "/Users/jonassenghaas/python/tryouts/file_manager/track_folder2"
folder_destination = "/Users/jonassenghaas/python/tryouts/file_manager/destination"

renamed_path = "Users/jonassenghaas/20|09|21 Test.py"

file = "itu 1,40,L9,Slides,Structuring Information3.png"
file_name, file_ext = os.path.splitext(file)
course, week = "".join(file_name.split(" ")[1:]).split(",")[0:2]

def format_itu(file):
	# extract file_name and path
	file_name, file_ext = os.path.splitext(file)
	was_renamed = re.search("^[A-Z]\d", file)
	print(was_renamed)

	if was_renamed:
	 	formatted_name = file 

	else:
		lecture, _type, name = "".join(file_name.split(" ")[1:]).split(",")[2:]
		formatted_name = "{} {}_{}{}".format(lecture.upper(), _type, name, file_ext)

	return formatted_name

print(format_itu(file))

# def rename(file):
# 	file_name, file_ext = os.path.splitext(file)
# 	match_itu = re.search("^itu", file_name)

# 	if match_itu:
# 		lecture, file, name = "".join(file_name.split(" ")[1:]).split(",")[2:]
					
# 		course_list = ["IDSP", "LA/O", "RBS"]
# 		course = course_list[int(course)-1]
# 		week = "Week {}".format(week)
# 		str(lecture.upper())

# 		new_name = "{} {}_{}{}".format(lecture, file, name, file_ext)
# 	else: 
# 		print("no renaming possible")

# 	return new_name

# print(rename(file))



# i=1
# file_exists = True

# if file_exists:
# 	for i in range(3):
# 		i += 1
# 	str = "{}{}{}".format(os.path.splitext(renamed_path)[0], str(i),os.path.splitext(renamed_path)[1])

# print(str)








# def sort_automation(path):
# 	for file in os.listdir(path):
# 		source_path = "{}/{}".format(path, file)
# 		new_path = "{}/{}".format(folder_destination, file)
# 		os.rename(source_path, new_path)
# 		print("File moved")

# def on_modified(event):
# 	print("A change to {} has been detected".format(event.src_path.split("/")[-1].upper()))
# 	sort_automation(event.src_path)

			
# def main():
# 	#initialize event handler as instance of class "FileSystemEventHandler"
# 	event_handler = FileSystemEventHandler()
# 	event_handler.on_modified = on_modified

# 	#initialize and start observer of downloads folder
# 	downloads_observer = Observer()
# 	downloads_observer.schedule(event_handler, downloads_folder, recursive=False)
# 	downloads_observer.start()

# 	#initialize and start observer of desktop folder
# 	desktop_observer = Observer()
# 	desktop_observer.schedule(event_handler, desktop_folder, recursive=False)
# 	desktop_observer.start()
	
# 	#stop both observers with keyboard interrupt
# 	try:
# 		while True:
# 			time.sleep(1)
# 	except KeyboardInterrupt:
# 			downloads_observer.stop()
# 			desktop_observer.stop()
# 	downloads_observer.join()
# 	desktop_observer.join()

# if __name__ == "__main__":
# 	print("Running...")
# 	main()





# def format_time():
# 	# create formatted time the when the file was moved 
# 	year, month, day = str(datetime.now()).split(" ")[0].split("-")
# 	formatted_time = "{}|{}|{}".format(year[2:], month, day)

# 	return formatted_time

# def rename(file):
# 	global new_name
# 	# extract file_name and path
# 	file_name, file_ext = os.path.splitext(file)

# 	# rename
# 	if file_ext != "":
# 		if re.search("^itu", file_name):
# 			course, week, lecture, file, name = file_name.split(" ")[1].split(",")
			
# 			course_list = ["IDSP", "LA/O", "RBS"]
# 			course = "{}".format(course_list[course+1])
# 			week = "Week {}".format(week)
# 			str(lecture.upper())

# 			new_name = "{} {}_{} - {}|{}".format(lecture, file, name, course, week)
		
# 		elif re.search("^Screenshot", file_name):
# 			new_name = "Screenshot"
			
# 		else: 
# 			new_name = "{} {}{}".format(format_time(), file_name.capitalize(), file_ext)
	
# 	else: 
# 			new_name = "{} {}".format(format_time(), file_name.capitalize())

# 	return new_name

# def sort_automation():
# 	for file in os.listdir(folder_to_track):
# 		new_name = rename(file)
# 		file_name, file_ext = os.path.splitext(new_name)

# 		source_path = os.path.abspath("{}/{}".format(folder_to_track, file))

# 		# if re.search("^Screenshot", file_name):
# 		# 	counter = 1
# 		# 	screen_directory = "{}/screenshots".format(folder_destination)
# 		# 	try: 
# 		# 		os.mkdir(screen_directory)
			
# 		# 	file_exists = os.path.isfile(screen_directory)
# 		# 	while file_exists:
# 		# 		i+=1
# 		# 		new_name = os.path.splitext("{}{}{}".format(filename, str(i), file_ext)
# 		# 		new_path = "{}/{}".format(screen_directory, new_name)
# 		# 		file_exists = os.path.isfile(new_path)

# 		# 	os.rename(source_path)

# 		#videos
# 		if file_ext == ".mp4":
# 			try: 
# 				os.mkdir("{}/video".format(folder_destination)) 
# 			except: None
			
# 			new_path = "{}/video/{}".format(folder_destination, new_name)
# 			os.rename(source_path, new_path)

# 		#photos
# 		elif file_ext == ".jpg" or file_ext == ".jpeg" or file_ext == ".gif" or file_ext == ".png":
# 			try:
# 				os.mkdir("{}/photos".format(folder_destination))
# 			except: None
# 			new_path = "{}/photos/{}".format(folder_destination, new_name)
# 			os.rename(source_path, new_path)

# 		#audio
# 		elif file_ext == ".mp3" or file_ext == ".wav":
# 			try:
# 				os.mkdir("{}/audio".format(folder_destination))
# 			except: None
# 			new_path = "{}/audio/{}".format(folder_destination, new_name)
# 			os.rename(source_path, new_path)

# 		#pdf's
# 		elif file_ext == ".pdf":
# 			try:
# 				os.mkdir("{}/pdf".format(folder_destination)) 
# 			except: None
# 			new_path = "{}/pdf/{}".format(folder_destination, new_name)
# 			os.rename(source_path, new_path)

# 		#creativity
# 		elif file_ext == ".psd":
# 			try:
# 				os.mkdir("{}/creativity".format(folder_destination)) 
# 			except: None
# 			new_path = "{}/creativity/{}".format(folder_destination, new_name)
# 			os.rename(source_path, new_path)

# 		#productivity
# 		elif file_ext == ".docx" or file_ext == ".xls" or file_ext == ".pptx" or file_ext == ".pages" or file_ext == ".numbers" or file_ext == ".key":
# 			try:
# 				os.mkdir("productivity")
# 			except: None
# 			new_path = "{}/productivity/{}".format(folder_destination, new_name)
# 			os.rename(source_path, new_path)

# 		#programming
# 		elif file_ext == ".py" or file_ext == ".csv" or file_ext == ".txt":
# 			try:
# 				os.mkdir("{}/programming".format(folder_destination)) 
# 			except: None
# 			new_path = "{}/programming/{}".format(folder_destination, new_name)
# 			os.rename(source_path, new_path)

# 		else:
# 			try:
# 				os.mkdir("{}/other".format(folder_destination)) 
# 			except: None
# 			new_path = "{}/other/{}".format(folder_destination, new_name)
# 			os.rename(source_path, new_path)
# 	print("Done!")

		
# def main():
# 	sort_automation()

# if  __name__ == "__main__":
# 	main()
