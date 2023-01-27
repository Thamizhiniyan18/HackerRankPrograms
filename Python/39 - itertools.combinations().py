# Link to Program : https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations

string, k = input().strip().split()
for i in range(int(k)):
    temp = []
    for each in list(combinations(string, i + 1)):
        temp.append(''.join(sorted(list(each))))
    print('\n'.join(sorted(temp)))
