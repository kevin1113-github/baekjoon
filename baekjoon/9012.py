import sys
input = sys.stdin.readline

T = int(input())

datas = [input().strip() for _ in range(T)]

for data in datas:
  stack = 0
  for c in data:
    if c == '(':
      stack += 1
    else:
      if stack <= 0:
        print('NO')
        break
      else:
        stack -= 1
  else:
    print('YES' if stack == 0 else 'NO')
