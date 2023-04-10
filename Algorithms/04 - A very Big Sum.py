# Link to Program : https://www.hackerrank.com/challenges/a-very-big-sum/problem


def aVeryBigSum(ar):
    return sum(ar)


if __name__ == '__main__':
    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    print(aVeryBigSum(ar))
