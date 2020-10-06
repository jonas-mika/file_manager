# README: FILE_MANAGER

## Description
This is an collaborative project of Frederik and Mika. The Sript aims to track folders and sort them depending according to a specific algorithm into a destination folder. Both the tracked_folders and the destination folder should be chosen by the User via a GUI. The program should be able to run in the background or do a cleanup from time to time, depending on the User preferences 

## TODO
Mika
- [ ] Make a GUI to choose path of both tracked and destination folder
- [ ] Make the program run on every OS and independent from the Python that it is installed on the local machine (Is this possible @Frederik?)
- [ ] Fix bug of failing downloads from webbrowser while script is running

Frederik
- [ ] The observable fires twice because it removes a file from the path it watches. That can be many events in a second if there is 100 files.
- [ ] Make strategies or pipes for different files.

## To Run

In shell type:
`source venv/bin/activate`
to activate the virtual environment.

Then type:
`python file_manager.py`
to run the program.

It will watch each folders(create observers) in sorting.json's "watch".
And it will match in sorting.json's "match".

The match-format will be:
`"regex": "destination folder"`

You can use `$USER` in your strings to use the current user on the computer.
This is encouraged, you can see examples in sorting.json.

To stop the program, press:
`ctrl + c`

To tear down the virtual environment type:
`deactivate`

Have fun!
