# Link to Program : https://www.hackerrank.com/challenges/insertionsort1/problem

def insertion_sort(size, array):
    element = array[size - 1]
    print(element)
    for index, each in enumerate(array):
        print(index, each)


if __name__ == "__main__":
    # n = int(input())
    # arr = list(map(int, input().strip().split()))
    insertion_sort(5, [1, 2, 4, 5, 3])
