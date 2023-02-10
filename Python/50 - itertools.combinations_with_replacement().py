# Link to Program : https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

from itertools import combinations_with_replacement

string = input().strip().split()
for each in sorted(list(map(sorted, (list(combinations_with_replacement(string[0], int(string[1]))))))):
    print(''.join(each))
