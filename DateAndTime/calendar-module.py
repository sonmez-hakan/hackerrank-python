from calendar import day_name, weekday

t = list(map(int, input().split()))
print(day_name[weekday(*(t[2:] + t[:2]))].upper())
