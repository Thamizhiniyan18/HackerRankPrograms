# Link to Program : https://www.hackerrank.com/challenges/time-conversion/problem

from datetime import datetime

print(datetime.strptime(input().strip(), "%I:%M:%S%p").strftime("%H:%M:%S"))

