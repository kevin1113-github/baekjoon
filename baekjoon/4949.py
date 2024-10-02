import sys
input = sys.stdin.readline

def isCorrect(string):
  stack = []
  for c in string:
    if c == '[' or c == '(':
      stack.append(c)
      continue
    elif c == ']':
      if len(stack) == 0 or stack.pop() != '[':
        return 'no'
    elif c == ')':
      if len(stack) == 0 or stack.pop() != '(':
        return 'no'
    else:
      continue
  if len(stack) != 0:
    return 'no'
  return 'yes'

strings = []

while True:
  string = input().strip('\n')
  if string == '.':
    break
  strings.append(string)

for string in strings:
  print(isCorrect(string))
