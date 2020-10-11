import pandas as pd 

data = pd.read_excel ('/mnt/f/Downloads/COVID-19+data+by+NHS+Board+11+October+2020.xlsx', skiprows=2, sheet_name='Table 1 - Cumulative cases')
df = pd.DataFrame(data, columns= ['NHS Lothian'])
dailyIncrease = df.loc[218] - df.loc[217] 
print(dailyIncrease.to_string())