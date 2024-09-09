import sys

# N 입력
N = int(sys.stdin.readline())
# N개의 수 입력
nums = [int(sys.stdin.readline()) for _ in range(N)]
# 정렬 내장함수로 오름차순 정렬
nums.sort()

# 정렬된 수 출력
for num in nums:
  print(num)
