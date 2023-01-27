# Link to Program : https://www.hackerrank.com/challenges/symmetric-difference/problem

m = int(input())
m_set = set(map(int, input().strip().split()))
n = int(input())
n_set = set(map(int, input().strip().split()))

print('\n'.join(str(each) for each in sorted(list(m_set.difference(n_set)) + list(n_set.difference(m_set)))))
