# Link to Program : https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    markSheet = []
    scores = []

    for i in range(0, int(input())):
        name = input()
        score = float(input())
        markSheet.append([name, score])
        scores.append(score)

    sec_low_grade = sorted(list(set(scores)))[1]

    for NAME, SCORE in sorted(markSheet):
        if SCORE == sec_low_grade:
            print(NAME)
