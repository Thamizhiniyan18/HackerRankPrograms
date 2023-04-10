# Link to Problem : https://www.hackerrank.com/challenges/designer-door-mat/problem

def main():
    n, m = map(int, input().split(' '))
    pattern = '.|.'
    middle_point = ((n - 1) / 2) + 1

    for i in range(n):
        if i + 1 < middle_point:
            print(f'{f"{pattern * i}" + pattern + f"{pattern * i}"}'.center(m, '-'))
        elif i + 1 == middle_point:
            print(f'WELCOME'.center(m, '-'))
        else:
            print(f'{f"{pattern * (n - (i + 1))}" + pattern + f"{pattern * (n - (i + 1))}"}'.center(m, '-'))

    # Another Method

    # N, M = map(int, input().split())
    # for i in range(1, N, 2):
    #     print((i * ".|.").center(M, "-"))
    # print("WELCOME".center(M, "-"))
    # for i in range(N - 2, -1, -2):
    #     print((i * ".|.").center(M, "-"))

if __name__ == "__main__":
    main()