# Daily Increase

A simple script to determine the daily increase of COVID-19 cases in NHS Scotland for the previous 24 hours

The script relies on the user putting the Excel file from the Scottish Government's website into a location and updating the script to the location. Currently the script will take away row 218 from 217 to provide the difference. 

My intention is to make the script more automatic through iteration to the point it will run automatically each day at 14:05 BST/GMT and download the file for the user.

I have now created excellist.py which uses lists locate the last two numbers, subtract them using numpy and then strip the array of brackets. Finally print is used to create the output message.

The file has been updated to pull the file down using an absolute path from the Scottish Government website.
