# Link to Program : https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = int(input())
numbers = set(map(int, input().strip().split()))
for _ in range(int(input())):
    command = input().strip().split()
    if command[0] == "remove":
        numbers.remove(int(command[1]))
    if command[0] == "discard":
        numbers.discard(int(command[1]))
    if command[0] == "pop":
        numbers.pop()
print(sum(numbers))
