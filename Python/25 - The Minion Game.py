# Link to program : https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    # your code goes here
    length_of_string = len(string)

    kev = sum(length_of_string - i for i in range(length_of_string) if string[i] in "AEIOU")
    stu = length_of_string * (length_of_string + 1) / 2 - kev

    if stu > kev:
        print(f"Stuart {int(stu)}")
    elif stu == kev:
        print("Draw")
    else:
        print(f"Kevin {int(kev)}")


if __name__ == '__main__':
    s = input()
    minion_game(s)
