self_num = [True] * 10001

for i in range(1, 10001):
  n = i
  for j in str(i):
    n += int(j)
  if n < 10001:
    self_num[n] = False

for i in range(1, 10001):
  if self_num[i]:
    print(i)
