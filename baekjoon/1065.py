import sys

N = int(sys.stdin.readline())

def is_hansu(n):
  if n < 100:
    return True
  else:
    n = str(n)
    diff = int(n[1]) - int(n[0])
    for i in range(2, len(n)):
      if int(n[i]) - int(n[i-1]) != diff:
        return False
    return True

count = 0
for i in range(1, N+1):
  if is_hansu(i):
    count += 1

print(count)
