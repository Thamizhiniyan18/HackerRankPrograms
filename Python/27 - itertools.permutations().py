# Link to Program : https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations

string, number = input().split()
print('\n'.join(''.join(each) for each in sorted(permutations(string, int(number)))))


