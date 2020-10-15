import pandas as pd #imports the various modules to allow the script to run
import numpy as np 
import requests
from datetime import datetime
import calendar
import os

y = input("Please name the excel file:") #asks the user for the file
print("Retreiving file and calculating the daily increase")

dateTimeObj = datetime.now() #retreives the date using datetime
timestampStr = dateTimeObj.strftime("%d %m %Y") #changes the date into a string
day = timestampStr[-10:-8] #slices the string to produce the 'day' value
year = timestampStr[-4:] #slices the string to produce the 'year' value
numberMonth = timestampStr[-7:-5] #slices the string to produce the 'month' value
intMonth = calendar.month_name[int(numberMonth)] #changes the sliced string 'month' value into a integer and uses calendar to transform this in the written month name
month = str(intMonth) #changes the month name back into a string

url = ('https://www.gov.scot/binaries/content/documents/govscot/publications/statistics/2020/04/coronavirus-covid-19-trends-in-daily-data/documents/covid-19-data-by-nhs-board/covid-19-data-by-nhs-board/govscot%3Adocument/COVID-19%2Bdaily%2Bdata%2B-%2Bby%2BNHS%2BBoard%2B-%2B'+day+'%2B'+month+'%2B'+year+'.xlsx')
r = requests.get(url) 

with open(y, 'wb') as f: #writes the file to the location the user specificed in y
    f.write(r.content)

print(r.status_code)
print(r.encoding)

data = pd.read_excel (y, skiprows=2, sheet_name='Table 1 - Cumulative cases') #reads the excel file and the specific sheet, skips initial two rows
df = pd.DataFrame(data, columns= ['NHS Lothian']) #reads the specific column needed

df_list = [df.columns.values.tolist()] + df.values.tolist() #formats into a list

df_val1 = df_list[-1] #indexes the last row
df_val2 = df_list[-2] #indexes the second last row
daily_increase = np.subtract(df_val1, df_val2) #subtracts the two values, finding daily increase
print("The daily increase of cases in NHS Lothian is:", str(daily_increase).lstrip('[').rstrip(']')) #strips the brackets from numpy output and prints it as a string
os.remove(y)
