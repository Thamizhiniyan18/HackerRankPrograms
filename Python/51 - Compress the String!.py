# Link to Program : https://www.hackerrank.com/challenges/compress-the-string/problem

from itertools import groupby

print(' '.join(f"({len(list(each[1]))}, {each[0]})" for each in groupby(input())))
