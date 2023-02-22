# Link to Program : https://www.hackerrank.com/challenges/plus-minus/problem

def plus_minus(size, array):
    positive = 0
    negative = 0
    zero = 0
    for each in array:
        if each < 0:
            negative += 1
        if each == 0:
            zero += 1
        if each > 0:
            positive += 1

    return "\n".join(map(str, ["%.6f" % round(positive / size, 6), "%.6f" % round(negative / size, 6), "%.6f" % round(zero / size, 6)]))


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().strip().split()))
