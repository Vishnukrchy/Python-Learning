#Python datetime 
#Python datetime module contains classes for handling date and time data. 
#The datetime module provides classes for handling date and time data.

# example get current date =>
import datetime

now = datetime.datetime.now()
print(now)# it will print current date and time
print(now.year,now.month,now.day,now.hour,now.minute,now.second,now.microsecond)

# example get current date =>

today=datetime.date.today()
print(today)
print(today.year,today.month,today.day)

# artribute of datetime =>
print(dir(datetime))

# Python datetime.date Class
# => The datetime.date class represents a date without a specific time.
# It is a built-in class in Python that represents a date in the Gregorian calendar.

# example get current date =>
import datetime