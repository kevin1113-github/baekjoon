import sys

T = int(sys.stdin.readline())
cases = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]

for H, W, N in cases:
  N -= 1
  floor = N % H + 1
  room = N // H + 1
  print(floor * 100 + room)
