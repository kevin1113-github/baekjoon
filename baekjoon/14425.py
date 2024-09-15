import sys

N, M = map(int, sys.stdin.readline().split())

S = set([sys.stdin.readline().strip() for _ in range(N)])
testStr = [sys.stdin.readline().strip() for _ in range(M)]

included = 0
for string in testStr:
  if string in S:
    included += 1
print(included)
