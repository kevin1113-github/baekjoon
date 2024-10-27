import sys

def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)

def lcm(a, b):
  return a * b // gcd(a, b)

a, b = map(int, sys.stdin.readline().split())

print(gcd(a, b))
print(lcm(a, b))
