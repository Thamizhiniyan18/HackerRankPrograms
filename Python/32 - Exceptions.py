# Link to Program : https://www.hackerrank.com/challenges/exceptions/problem

for i in range(int(input())):
    try:
        a, b = map(str, input().strip().split(' '))
        print(int(a) // int(b))
    except ValueError as e:
        print(f"Error Code: {e}")
    except ZeroDivisionError as e:
        print(f"Error Code: {e}")
