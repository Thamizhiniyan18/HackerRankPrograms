# Link to Program : https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    l = len(bin(number)[2:])
    for i in range(1, number + 1):
        print(f"{f'{i}'.rjust(l)} {f'{oct(i)}'[2:].rjust(l)} {f'{hex(i)}'[2:].upper().rjust(l)} {f'{bin(i)}'[2:].rjust(l)}" )

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)