# Link to Program : https://www.hackerrank.com/challenges/list-comprehensions/problem

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    lists = []

    for i in range(0, x + 1):
        for j in range(0, y + 1):
            for k in range(0, z + 1):
                lists.append([i, j, k])

    newList = [x for x in lists if sum(x) != n]

    print(newList)
