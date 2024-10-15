import sys

N = int(sys.stdin.readline())
cases = [sys.stdin.readline().strip() for _ in range(N)]

for case in cases:
  score = 0
  cnt = 0
  for c in case:
    if c == 'O':
      cnt += 1
      score += cnt
    else:
      cnt = 0
  print(score)
