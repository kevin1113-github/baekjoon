import sys

C = int(sys.stdin.readline())

scoreList = [list(map(int, sys.stdin.readline().split())) for _ in range(C)]

for score in scoreList:
  N = score[0]
  scores = score[1:]
  avg = sum(scores) / N
  cnt = 0
  for s in scores:
      if s > avg:
          cnt += 1
  print(f"{cnt / N * 100:.3f}%")
