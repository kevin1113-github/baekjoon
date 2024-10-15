import sys

A = int(sys.stdin.readline().strip())
B = int(sys.stdin.readline().strip())
C = int(sys.stdin.readline().strip())

result = A * B * C

result = str(result)

for i in range(10):
  print(result.count(str(i)))
