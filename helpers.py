import datetime
import re
import os
import pwd

def get_user():
	return pwd.getpwuid( os.getuid() )[ 0 ]

def filter_variables(text, paths={}):
	for p in paths:
		text = text.replace(p, paths[p])
	return text.replace('$USER', get_user())


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