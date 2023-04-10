# Link to Program : https://www.hackerrank.com/challenges/py-set-union/problem

n = int(input())
english_newspaper = set(map(int, input().strip().split()))
m = int(input())
french_newspaper = set(map(int, input().strip().split()))
print(len(english_newspaper.union(french_newspaper)))
