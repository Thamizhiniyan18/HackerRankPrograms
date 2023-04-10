# Link to Program : https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict

ordered_dict = OrderedDict()

for _ in range(int(input())):
    temp = input().strip().rsplit(maxsplit=1)
    if temp[0] in ordered_dict:
        ordered_dict[temp[0]] += int(temp[1])
    else:
        ordered_dict[temp[0]] = int(temp[1])

for each in ordered_dict.items():
    print(*each)
