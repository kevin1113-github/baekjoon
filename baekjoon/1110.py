import sys

N = int(sys.stdin.readline())

nums = [N//10, N%10]

count = 0

while True:
  count += 1
  nums = [nums[1], (nums[0] + nums[1]) % 10]
  if N == nums[0] * 10 + nums[1]:
    break

print(count)
