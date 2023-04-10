# Link to Program : https://www.hackerrank.com/challenges/py-set-mutations/problem

n = int(input())
set_a = set(map(int, input().strip().split()))
for _ in range(int(input())):
    command = input().strip().split()
    set_b = set(map(int, input().strip().split()))
    if command[0] == "intersection_update":
        set_a.intersection_update(set_b)
    if command[0] == "symmetric_difference_update":
        set_a.symmetric_difference_update(set_b)
    if command[0] == "difference_update":
        set_a.difference_update(set_b)
    if command[0] == "update":
        set_a.update(set_b)
print(sum(set_a))
