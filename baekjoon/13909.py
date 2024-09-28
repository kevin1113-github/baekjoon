import sys

N = int(sys.stdin.readline())

cnt = 0
x = 1
while x**2 <= N:
  cnt += 1
  x += 1

print(cnt)
