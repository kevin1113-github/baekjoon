import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

queue = deque([i for i in range(1, N+1)])

result = []

while queue:
  for _ in range(K-1):
    queue.append(queue.popleft())
  result.append(queue.popleft())

print('<' + ', '.join(map(str, result)) + '>')
