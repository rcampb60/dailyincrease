from datetime import datetime
import calendar

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d %m %Y")

#print(timestampStr)

day = timestampStr[-10:-8]
year = timestampStr[-4:]
numberMonth = timestampStr[-7:-5]
intMonth = calendar.month_name[int(numberMonth)]
month = str(intMonth)

print(day, month, year)
print(day + "%2B" + month + "%2B" + year)
# +x+'%2B'+y+'%2B'+z+'.xlsx'