import sys

N, M = map(int, sys.stdin.readline().split())

pokemon = {}
for i in range(1, N+1):
  num = str(i)
  name = sys.stdin.readline().strip()
  pokemon[name] = num
  pokemon[num] = name

answer = [pokemon[sys.stdin.readline().strip()] for _ in range(M)]

print('\n'.join(answer))
