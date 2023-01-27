# Link to Program : https://www.hackerrank.com/challenges/python-time-delta/problem

# Complete the time_delta function below.
import datetime


def time_delta(t1, t2):
    time_format = '%a %d %B %Y %H:%M:%S %z'
    time1 = datetime.datetime.strptime(t1, time_format)
    time2 = datetime.datetime.strptime(t2, time_format)
    print(int((abs(time1 - time2)).total_seconds()))


if __name__ == '__main__':
    for _ in range(int(input())):
        time_delta(input(), input())
