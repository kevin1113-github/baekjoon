import sys
input = sys.stdin.readline

def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

prime_table = [1 if is_prime(i+1) else 0 for i in range(123456*2)]
T = []

while True:
  n = int(input())
  if n == 0:
    break
  T.append(n)

# for n in T:
#   cnt = 0
#   for i in range(n, n*2+1):
#     if is_prime(i):
#       cnt += 1
#   print(cnt)

for n in T:
  print(sum(prime_table[n:n*2]))
