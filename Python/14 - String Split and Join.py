# Link to Program : https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    # Method 1
    return '-'.join(line.split())

    # Method 2
    # return ''.join(each if each != " " else "-" for each in line)

    # Method 3
    # return line.replace(' ', '-')

if __name__ == '__main__':
    line = "this is a string"
    print(split_and_join(line.strip()))