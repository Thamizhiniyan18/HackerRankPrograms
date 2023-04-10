# Link to Program : https://www.hackerrank.com/challenges/birthday-cake-candles/problem

def birthdayCakeCandles(size, candles):
    return candles.count(max(candles))


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print(birthdayCakeCandles(n, arr))

