# Daily Increase

A simple script to determine the daily increase of COVID-19 cases in NHS Lothian for the previous 24 hours.

The user is asked to provide a name for the Excel file which is downloaded into the scripts' directory, read and then deleted. The script then produces the output. 

Recent updates have allowed the script to determine the date from the user's system clock. The date data is then manipulated and inserted into the hard-coded URL to allow Requests to pull the file down. 

# Installation

* Ensure you have [poetry](https://python-poetry.org/) installed on your system 
* Open a terminal and go to your version of the code locally
* Run `poetry install`
* Run `poetry shell`
* Run the script to load the Poetry env `poetry run vscode` (see [Workaround issue #8372](https://github.com/microsoft/vscode-python/issues/8372))
* Open vscode from the command line `code .`
* Select the interpreter (should be under your home directory: `~/.cache/pypoetry/virtualenvs/dailyincrease-<.....>-py3.8/bin/python`)

# Dev

If you are contributing to this repo, you can add yourself to the list of authors by running: `poetry run update_authors`
