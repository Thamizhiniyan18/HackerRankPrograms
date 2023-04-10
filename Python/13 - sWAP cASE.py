# Link to Program : https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    # Method One
    return s.swapcase()

    # Method Two
    # return ''.join(each.upper() if each.islower() else each.lower() for each in s)

if __name__ == '__main__':
    s = 'HackerRank.com presents "Pythonist 2".'
    print(swap_case(s))