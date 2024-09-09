
# 리스트 선언
li = [[5, 'r'], [3, 'g'], [6, 'b'], [1, 'y'], [2, 'p'], [4, 'o']]

# 정렬 전 리스트 출력
print(li)

# 정렬 내장함수로 각 요소의 [0] 값을 기준으로 내림차순 정렬
li.sort(key=lambda x: x[0], reverse=True)

# 정렬 후 리스트 출력
print(li)
