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

# Open Configuration File 
with open('./sorting.json', 'r') as f:
	CONFIG = json.load(f)

# Move and rename file
def move_file(src, file, dest):
	try: os.makedirs(f'{dest}')
	except: None

	os.rename(f'{src}/{file}', f'{dest}/{file}')
	print(f">>> moved {file} to <{dest}>")

#Driver Code, when watchdogs recognizes change in tracked folders
def on_modified(event):
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