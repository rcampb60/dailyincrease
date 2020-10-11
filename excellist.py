import pandas as pd #imports Pandas to use read_excel to read the excel file
import numpy as np #imports numpy to allow for subtraction of the rows
import requests #imports requests to allow for downloading of the excel file from the website directly

x = input("Please provide the relevant path to the COVID-19 Data by NHS Board Excel file on the Scottish Government's website: ") #this is the path to the file, found by right clicking
y = input("Please provide the path, including filename AND extension, which you wish to use: ") #this asks the user to input the location of the download, and to specific the file name and extension

print('Beginning file download with requests')

url = x #uses the users input to provide the URL to the get request
r = requests.get(url) 

with open(y, 'wb') as f: #writes the file to the location the user specificed in y
    f.write(r.content)

# Retrieve HTTP meta-data
print(r.status_code)
print(r.encoding)

data = pd.read_excel (y, skiprows=2, sheet_name='Table 1 - Cumulative cases') #reads the excel file and the specific sheet, skips initial two rows
df = pd.DataFrame(data, columns= ['NHS Lothian']) #reads the specific column needed

df_list = [df.columns.values.tolist()] + df.values.tolist() #formats into a list

df_val1 = df_list[-1] #indexes the last row
df_val2 = df_list[-2] #indexes the second last row
daily_increase = np.subtract(df_val1, df_val2) #subtracts the two values, finding daily increase
print("The daily increase of cases in NHS Lothian is:", str(daily_increase).lstrip('[').rstrip(']')) #strips the brackets from numpy output and prints it as a string



