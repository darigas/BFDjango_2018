import calendar

m, d, y = input().split()

print(calendar.day_name[calendar.weekday(int(y), int(m), int(d))].upper())