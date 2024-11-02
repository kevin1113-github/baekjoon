import sys

T = int(sys.stdin.readline())

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

test_cases = [map(int, sys.stdin.readline().split()) for _ in range(T)]

for test_case in test_cases:
  N, M = test_case
  print(factorial(M) // (factorial(N) * factorial(M-N)))
