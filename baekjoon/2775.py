import sys

T = int(sys.stdin.readline())
k_list, n_list = [], []

for _ in range(T):
  k_list.append(int(sys.stdin.readline()))
  n_list.append(int(sys.stdin.readline()))

for k, n in zip(k_list, n_list):
  people = [i+1 for i in range(n)]  # 0층 0 ~ n-1호까지 사람들
  for _ in range(k):
    for j in range(1, n):
      people[j] += people[j-1]
  print(people[-1])

# ...
# 4층   1   6  21  56 126 252 462
# 3층   1   5  15  35  70 126 210
# 2층   1   4  10  20  35  56  84
# 1층   1   3   6  10  15  21  28
# 0층   1   2   3   4   5   6   7 ...
