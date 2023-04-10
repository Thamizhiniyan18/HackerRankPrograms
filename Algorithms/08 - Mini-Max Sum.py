# Link to Program : https://www.hackerrank.com/challenges/mini-max-sum/problem

from itertools import combinations


def miniMaxSum(array):
    sums = list(map(sum, list(combinations(array, 4))))
    return f"{min(sums)} {max(sums)}"


if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    print(miniMaxSum(arr))
