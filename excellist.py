import pandas as pd 
import numpy as np
import requests

print('Beginning file download with requests')


url = 'https://www.gov.scot/binaries/content/documents/govscot/publications/statistics/2020/04/coronavirus-covid-19-trends-in-daily-data/documents/covid-19-data-by-nhs-board/covid-19-data-by-nhs-board/govscot%3Adocument/COVID-19%2Bdata%2Bby%2BNHS%2BBoard%2B11%2BOctober%2B2020.xlsx'
r = requests.get(url)

with open('/mnt/f/Downloads/11102020.xlsx', 'wb') as f:
    f.write(r.content)

# Retrieve HTTP meta-data
print(r.status_code)
print(r.encoding)

data = pd.read_excel ('/mnt/f/Downloads/11102020.xlsx', skiprows=2, sheet_name='Table 1 - Cumulative cases')
df = pd.DataFrame(data, columns= ['NHS Lothian'])

df_list = [df.columns.values.tolist()] + df.values.tolist()

df_val1 = df_list[-1]
df_val2 = df_list[-2]
daily_increase = np.subtract(df_val1, df_val2)
print("The daily increase of cases in NHS Lothian is:", str(daily_increase).lstrip('[').rstrip(']'))



