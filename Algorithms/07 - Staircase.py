# Link to Program : https://www.hackerrank.com/challenges/staircase/problem

n = int(input())
for i in range(n):
    print(f"{'#'* (i+1)}".rjust(n))
