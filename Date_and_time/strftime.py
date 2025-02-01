#Python strftime()
#Python strftime() function is used to format the date and time.

import datetime

now = datetime.datetime.now()

year = now.strftime("%Y")
print("year:", year)
month = now.strftime("%m")
print("month:", month)
day = now.strftime("%d")
print("day:", day)
time = now.strftime("%H:%M:%S")
print("time:", time)
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)	

print(now.strftime("%Y-%m-%d %H:%M:%S"))


#example 2   Creating string from a timestamp =>
from datetime import datetime

timestamp

