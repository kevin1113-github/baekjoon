import sys

def factorial(n):
  if n == 0:
    return 1
  return n * factorial(n - 1)

n, k = map(int, sys.stdin.readline().split())

print(factorial(n) // (factorial(k) * factorial(n - k)))
