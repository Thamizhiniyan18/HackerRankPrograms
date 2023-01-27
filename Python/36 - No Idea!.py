# Link to Program : https://www.hackerrank.com/challenges/no-idea/problem

n, m = map(int, input().strip().split())
N = list(map(int, input().strip().split()))
A = set(map(int, input().strip().split()))
B = set(map(int, input().strip().split()))
happiness = 0

for each in N:
    if each in A:
        happiness += 1
    elif each in B:
        happiness -= 1

print(happiness)