# Link to Program : https://www.hackerrank.com/challenges/compare-the-triplets/problem

def compareTriplets(a, b):
    result = [0, 0]
    for i in range(len(a)):
        if a[i] > b[i]:
            result[0] += 1
        elif a[i] < b[i]:
            result[1] += 1
    return result


if __name__ == '__main__':
    A = list(map(int, input().rstrip().split()))
    B = list(map(int, input().rstrip().split()))
    print(" ".join(map(str, compareTriplets(A, B))))
