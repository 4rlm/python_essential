## W3 Schools TUTORIAL: https://www.w3schools.com/python/python_datetime.asp
####################################

## 1. == Python Dates:
import datetime
date_1 = datetime.datetime.now()
print(date_1)     #format: 2018-10-21 03:32:55.644169
print(date_1.year)
print(date_1.strftime("%A"))
####################################

## 3. == Creating Date Objects:
## The datetime() class requires three parameters to create a date: year, month, day.
## The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).
date_2 = datetime.datetime(2020, 5, 17)
print(date_2)
####################################


## 3. == The strftime() Method:
## Display the name of the month:
date_3 = datetime.datetime(2018, 6, 1)
print(date_3.strftime("%B"))
####################################


## 4. == XXX:
####################################


## 5. == XXX:
####################################
