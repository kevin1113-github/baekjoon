import sys

N = int(sys.stdin.readline())

points = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]

points.sort(key=lambda x: (x[1], x[0]))

for point in points:
  print(*point)