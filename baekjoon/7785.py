import sys

n = int(sys.stdin.readline())
remain = set()

for i in range(n):
  string = sys.stdin.readline().split()
  if string[1] == 'enter':
    remain.add(string[0])
  else:
    remain.remove(string[0])

remain = sorted(list(remain), reverse=True)
print (*remain, sep='\n')
