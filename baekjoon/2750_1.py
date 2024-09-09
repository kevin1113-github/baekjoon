import sys

# 정렬 함수
def sortNums(nums):
  # 선택 정렬
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      # i번째 수가 j번째 수보다 크다면
      if nums[i] > nums[j]:
        # 두 수의 위치를 바꿈
        nums[i], nums[j] = nums[j], nums[i]
  # 정렬된 수 반환
  return nums

# N 입력
N = int(sys.stdin.readline())
# N개의 수 입력
nums = [int(sys.stdin.readline()) for _ in range(N)]
# 정렬 내장함수로 오름차순 정렬
nums = sortNums(nums)

# 정렬된 수 출력
for num in nums:
  print(num)
