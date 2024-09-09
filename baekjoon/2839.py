import sys

N = int(sys.stdin.readline()) # 설탕의 총 무게 N kg 입력
answer = -1                   # 정답은 -1로 초기화

fiveKG = N//5                 # 5kg 봉지로 나눴을 때의 몫

while fiveKG > 0:             # 5kg 봉지 갯수를 하나씩 줄여가며 반복
  left = N-(fiveKG*5)         # 5kg 봉지에 담고 남은 나머지
  if left%3 == 0:             # 나머지가 3kg 봉지에 남김없이 담긴다면
    answer = fiveKG + left//3 # 정답 저장
    break                     # 반복문 탈출
  else:                       # 아니라면
    fiveKG -= 1               # 5kg 봉지 줄이기
else:                         # 5kg 봉지가 0이 되어 반복문을 빠져나온 경우
  if N%3 == 0:                # 설탕이 모두 3kg 봉투에 남김없이 들어가면
    answer = N//3             # 정답 저장

print(answer)                 # 정답 출력
