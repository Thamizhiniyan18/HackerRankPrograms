# Link to Program : https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())

    LIST = list()

    for _ in range(N):
        instruction = input().strip().split(' ')

        if instruction[0] == "insert":
            LIST.insert(int(instruction[1]), int(instruction[2]))

        elif instruction[0] == "remove":
            LIST.remove(int(instruction[1]))

        elif instruction[0] == "append":
            LIST.append(int(instruction[1]))

        elif instruction[0] == "sort":
            LIST.sort()

        elif instruction[0] == "pop":
            LIST.pop()

        elif instruction[0] == "reverse":
            LIST.reverse()

        elif instruction[0] == "print":
            print(LIST)

