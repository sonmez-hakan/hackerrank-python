from calendar import *

month, day, year = map(int, input().split())
weekday_index = weekday(year, month, day)
print(day_name[weekday_index].upper())
