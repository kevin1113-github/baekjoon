import sys

expression = sys.stdin.readline().strip().split('-')
result = sum(map(int, expression[0].split('+')))

for i in expression[1:]:
  result -= sum(map(int, i.split('+')))
                
print(result)