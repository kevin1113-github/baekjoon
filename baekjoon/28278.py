import sys

N = int(sys.stdin.readline())
commands = [sys.stdin.readline().strip() for _ in range(N)]

stack = []

for command in commands:
  if command.startswith('1'):
    X = int(command[2:])
    stack.append(X)
  elif command == '2':
    if len(stack) > 0:
      print(stack.pop())
    else:
      print(-1)
  elif command == '3':
    print(len(stack))
  elif command == '4':
    if len(stack) == 0:
      print(1)
    else:
      print(0)
  elif command == '5':
    if len(stack) > 0:
      print(stack[-1])
    else:
      print(-1)
