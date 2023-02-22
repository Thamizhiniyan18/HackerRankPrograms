# Link to Program : https://www.hackerrank.com/challenges/big-sorting/problem
def bigSorting(unsorted):
    return sorted(unsorted, key=int)


if __name__ == "__main__":
    arr = []
    for _ in range(int(input())):
        arr.append(input().strip())

    print("\n".join(list(map(str, bigSorting(arr)))))
