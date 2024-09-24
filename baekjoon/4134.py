import sys

def is_prime(num):
  if num <= 1:
    return False
  if num == 2:
    return True
  if num % 2 == 0:
    return False
  for i in range(3, int(num**0.5)+1):
    if num % i == 0:
      return False
  return True

N = int(sys.stdin.readline())
n = [int(sys.stdin.readline()) for _ in range(N)]

for i in n:
  num = i
  while True:
    if num == 0 or num == 1:
      print(2)
      break
    if is_prime(num):
      print(num)
      break
    else:
      num += 1
