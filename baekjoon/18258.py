from collections import deque
import sys

def queue(q, inst):
  if inst[0] == 'push':
    q.append(inst[1])
  elif inst[0] == 'pop':
    print(q.popleft() if q else -1)
  elif inst[0] == 'size':
    print(len(q))
  elif inst[0] == 'empty':
    print(0 if q else 1)
  elif inst[0] == 'front':
    print(q[0] if q else -1)
  elif inst[0] == 'back':
    print(q[-1] if q else -1)

N = int(sys.stdin.readline())
q = deque()

for _ in range(N):
  inst = sys.stdin.readline().split()
  queue(q, inst)
