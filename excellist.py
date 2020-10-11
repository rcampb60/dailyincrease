import pandas as pd 
import numpy as np

data = pd.read_excel ('/mnt/f/Downloads/COVID-19+data+by+NHS+Board+11+October+2020.xlsx', skiprows=2, sheet_name='Table 1 - Cumulative cases')
df = pd.DataFrame(data, columns= ['NHS Lothian'])

df_list = [df.columns.values.tolist()] + df.values.tolist()

df_val1 = df_list[-1]
df_val2 = df_list[-2]
daily_increase = np.subtract(df_val1, df_val2)
print("The daily increase of cases in NHS Lothian is:", str(daily_increase).lstrip('[').rstrip(']'))



