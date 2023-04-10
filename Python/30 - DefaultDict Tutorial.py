# Link to Program : https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

from collections import defaultdict

a, b = map(int, input().split(' '))
default_Dict = defaultdict(list)

for i in range(a):
    temp = input()
    default_Dict[temp].append(i + 1)

for each in [input() for i in range(b)]:
    print(' '.join(map(str, default_Dict[each])) if default_Dict[each] else '-1')
