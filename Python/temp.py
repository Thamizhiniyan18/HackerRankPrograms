# n = int(input())
n = 5
ls = []

for i in range(n):
    for j in range(i + 1):
        temp = (j + 1) % 2
        if temp != 0:
            ls.insert(0, "1")
        else:
            ls.insert(0, "0")
        print(ls)
    print()
