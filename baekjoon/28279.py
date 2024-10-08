import sys
from collections import deque

N = int(sys.stdin.readline())
commands = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

queue = deque()

for command in commands:
  cmd = command[0]
  if cmd == 1:
    queue.appendleft(command[1])
  elif cmd == 2:
    queue.append(command[1])
  elif cmd == 3:
    print(queue.popleft() if queue else -1)
  elif cmd == 4:
    print(queue.pop() if queue else -1)
  elif cmd == 5:
    print(len(queue))
  elif cmd == 6:
    print(1 if not queue else 0)
  elif cmd == 7:
    print(queue[0] if queue else -1)
  elif cmd == 8:
    print(queue[-1] if queue else -1)
