import sys
input = sys.stdin.readline

K = int(input())
N = [int(input()) for _ in range(K)]

stack = []

for n in N:
  if n == 0:
    stack.pop()
  else:
    stack.append(n)

print(sum(stack))
