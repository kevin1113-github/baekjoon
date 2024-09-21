import sys

def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a % b)

def lcm(a, b):
  return a * b // gcd(a, b)

A, B = map(int, sys.stdin.readline().split())
print(lcm(A, B))
