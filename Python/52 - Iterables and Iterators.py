# Link to Program : https://www.hackerrank.com/challenges/iterables-and-iterators/problem

import itertools

# for index, each in enumerate(itertools.cycle('abcd')):
#     if index < 20:
#         print(each)
#     else:
#         break

for each in itertools.repeat(20, 4):
    print(each)
