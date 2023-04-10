# Link to Program : https://www.hackerrank.com/challenges/capitalize/problem

def solve(s):
    # Hacker Rank Solution Starts
    return ' '.join([each.capitalize() for each in s.strip().split(' ')])
    # Hacker Rank Solution Ends


def main():
    s = input()
    print(solve(s))


if __name__ == "__main__":
    main()
