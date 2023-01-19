# Link to Program : https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple

# Method 1
n = int(input())
student = namedtuple('student', input().strip().split())
list_of_students = [student(*input().strip().split()) for _ in range(n)]
print('%.2f' % (sum(int(each.MARKS) for each in list_of_students) / n))

# Method 2
# n, temp, summation = int(input()), list(input().split()), 0
# for i in range(n):
#     summation += int(list(input().split())[temp.index('MARKS')])
# print(summation / n)
