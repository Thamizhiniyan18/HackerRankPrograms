# Link to Program : https://www.hackerrank.com/challenges/diagonal-difference/problem

def diagonal_difference(array):
    diagonal1 = 0
    diagonal2 = 0
    for j in range(len(array)):
        diagonal1 += array[j][j]
        diagonal2 += array[(len(array) - 1) - j][j]

    return abs(diagonal1 - diagonal2)


if __name__ == "__main__":
    arr = []

    for i in range(int(input())):
        arr.append(list(map(int, input().strip().split())))

    print(diagonal_difference(arr))
