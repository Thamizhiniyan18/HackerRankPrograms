# Link to Program : https://www.hackerrank.com/challenges/polar-coordinates/problem

from cmath import phase

complex_number = complex(input().strip())
print(f"{abs(complex(complex_number))}\n{phase(complex(complex_number))}")
