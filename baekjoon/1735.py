import sys

def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a % b)

a1, b1 = map(int, sys.stdin.readline().split())
a2, b2 = map(int, sys.stdin.readline().split())

a3, b3 = a1 * b2 + a2 * b1, b1 * b2

g = gcd(a3, b3)

print(a3 // g, b3 // g)
