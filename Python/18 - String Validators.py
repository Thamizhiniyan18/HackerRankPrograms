# Link to Program : https://www.hackerrank.com/challenges/string-validators/problem


def isAlphaNumeric(s):
    for i in s:
        if i.isalnum():
            return True
    return False

def isAlphabetic(s):
    for i in s:
        if i.isalpha():
            return True
    return False

def isDigit(s):
    for i in s:
        if i.isdigit():
            return True
    return False

def isLower(s):
    for i in s:
        if i.islower():
            return True
    return False

def isUpper(s):
    for i in s:
        if i.isupper():
            return True
    return False


if __name__ == '__main__':
    # s = input()
    s = 'qA2'

    print(isAlphaNumeric(s))
    print(isAlphabetic(s))
    print(isDigit(s))
    print(isLower(s))
    print(isUpper(s))