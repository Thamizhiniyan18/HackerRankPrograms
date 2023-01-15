# Link to Program : https://www.hackerrank.com/challenges/alphabet-rangoli/problem

import string


def print_rangoli(size):
    alphabets = string.ascii_lowercase

    ascending_list = list(alphabets[0: size])
    descending_list = list(reversed(ascending_list))
    ascending_string = ''.join(ascending_list)
    descending_string = ''.join(descending_list)
    temp = []

    for i in range(size):
        temp.append('-'.join(list(f"{descending_string[0: i]}{descending_list[i]}{ascending_string[size - i:size]}")))

    for i in range(size - 1):
        temp.append('-'.join(list(f"{descending_string[0: (size - 2) - i]}{list(ascending_list[1:size])[i]}{ascending_string[i + 2:size]}")))

    s = ''

    for each in temp:
        s = s + each.center(len(temp[size - 1]), '-') + '\n'

    return s


if __name__ == '__main__':
    n = int(input())
    print(print_rangoli(n))
