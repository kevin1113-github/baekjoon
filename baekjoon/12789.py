import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

line = nums
stack = []

cnt = 1
while cnt <= N:
  if stack and stack[-1] == cnt:
    stack.pop()
    cnt += 1
    continue
  elif not line:
    break
  elif line[0] == cnt:
    line.pop(0)
    cnt += 1
    continue
  else:
    stack.append(line.pop(0))
    continue

if cnt <= N:
  print("Sad")
else:
  print("Nice")
