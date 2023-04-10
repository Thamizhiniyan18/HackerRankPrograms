# Link to program :https://www.hackerrank.com/challenges/itertools-product/problem

import itertools

a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))

# Method 1

print(' '.join(map(str, itertools.product(a, b))))


# Method 2

# for each in list(itertools.product(a, b)):
#     print(each, end=' ')


# Method 3

# print(' '.join(str(each) for each in list(itertools.product(a, b))))





