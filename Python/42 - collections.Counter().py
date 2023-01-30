# Link to Program : https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

number_of_shoes = int(input())
available_shoe_sizes = Counter(map(int, input().strip().split()))
total_money_earned = 0
for _ in range(int(input())):
    size, price = map(int, input().strip().split())
    if available_shoe_sizes[size] != 0 and size in available_shoe_sizes.keys():
        available_shoe_sizes[size] -= 1
        total_money_earned += price

print(total_money_earned)
