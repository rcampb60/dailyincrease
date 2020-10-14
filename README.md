# Daily Increase

A simple script to determine the daily increase of COVID-19 cases in NHS Lothian for the previous 24 hours

The user is asked for the location of the Excel document. This can be obtained by navigating to https://www.gov.scot/publications/coronavirus-covid-19-trends-in-daily-data/ after 2pm BST each day then right clicking on the COVID-19 Data by NHS Board [RELEVANT DATE HERE] file and clicking 'copy path'. 

The user is then asked for the filename, extension and download path. The path should be along the lines of /user/downloads/filename.xlsx and should be unique. Personally I've used the format DDMMYYYY.xlsx for clarity. 

The script uses a combination of Pandas (to read the Xlsx data) and Numpy (to find the difference) as well as Requests to enable the file download.

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
