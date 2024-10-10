import sys
from collections import deque

N = int(sys.stdin.readline())

balloons = list(map(int, sys.stdin.readline().split()))
queue = deque([i for i in range(1, N+1)])

result = []

result.append(queue.popleft())

while queue:
  move = balloons[result[-1]-1]
  reverse = move < 0
  for _ in range(abs(move)-1):
    if reverse:
      queue.appendleft(queue.pop())
    else:
      queue.append(queue.popleft())
  if reverse:
    result.append(queue.pop())
  else:
    result.append(queue.popleft())

print(' '.join(map(str, result)))
