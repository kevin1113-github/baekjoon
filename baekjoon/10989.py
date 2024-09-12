import sys

# 자연수 개수 N 입력
N = int(sys.stdin.readline())
# 1부터 10000까지의 숫자 개수를 저장할 리스트 생성, 초기화
numbers = [0] * 10000

# N개의 자연수 입력
for _ in range(N):
  # 입력받은 자연수 - 1 인덱스에 1 추가
  numbers[int(sys.stdin.readline()) - 1] += 1

# 1부터 10000까지의 숫자를 순서대로 출력
for i in range(10000):
  # 해당 숫자가 0보다 클때만 출력
  if numbers[i] > 0:
    # 해당 인덱스의 반복 횟수만큼 해당 숫자 출력
    for _ in range(numbers[i]):
      print(i + 1)
