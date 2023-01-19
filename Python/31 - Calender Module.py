# Link to Program : https://www.hackerrank.com/challenges/calendar-module/problem

import calendar

month, date, year = map(int, input().strip().split(' '))
print(list(calendar.day_name)[calendar.weekday(year, month, date)].upper())

