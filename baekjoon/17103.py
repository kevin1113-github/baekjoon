import sys
input = sys.stdin.readline

def is_prime(n):
  if n <= 1:
    return False
  if n % 2 == 0:
    return False
  for i in range(3, int(n**0.5)+1, 2):
    if n % i == 0:
      return False
  return True

prime_table = {i:is_prime(i) for i in range(3, 1000000, 2)}

def goldbach(n):
  if n == 4:
    return 1

  cnt = 0
  for i in range(3, n//2+1, 2):
    if prime_table[i] and prime_table[n-i]:
      cnt += 1
  return cnt

T = int(input())

for _ in range(T):
  print(goldbach(int(input())))
