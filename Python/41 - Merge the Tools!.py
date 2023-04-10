# Link to Program : https://www.hackerrank.com/challenges/merge-the-tools/problem
from collections import OrderedDict


def merge_the_tools(string, k):
    for i in range(0, len(string.strip()), k):
        print(''.join(list(OrderedDict.fromkeys(string[i: i + k]).keys())))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
