# Link to Program : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))[:n]
    print(sorted(list(set(arr)))[-2])
