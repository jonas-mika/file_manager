# README

## TODO

- [x] Fix @paths.
- [x] Make directory creation recursive.

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
