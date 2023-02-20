from datetime import date, timedelta
#1
dt = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date :',dt)
#2
print('Yesterday:', date.today() - timedelta(1))
print('Today:', date.today())
print('Tomorrow:', date.today() + timedelta(1))
#3
import datetime
dt = datetime.datetime.today().replace(microsecond=0)
print(dt)
#4
from datetime import datetime, time
def date_diff_in_Seconds(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds
date1 = datetime.strptime('2023-02-01 17:30:00', '%Y-%m-%d %H:%M:%S')
date2 = datetime.now()
print("\n%d seconds" %(date_diff_in_Seconds(date2, date1)))