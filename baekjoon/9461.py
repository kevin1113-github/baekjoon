import sys

T = int(sys.stdin.readline())
N = [int(sys.stdin.readline()) for _ in range(T)]

dp = [0] * 101
dp[1], dp[2], dp[3], dp[4], dp[5] = 1, 1, 1, 2, 2
for i in range(6, 101):
  dp[i] = dp[i-1] + dp[i-5]

for n in N:
  print(dp[n])
