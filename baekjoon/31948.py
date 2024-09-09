import sys

def countWords(str):
  i = 0
  count = 0
  while i < len(str):
    start = i
    while str[i] == str[start]:
      i += 1
      if i >= len(str):
        break
    count += 1
  return count-1 if '?' in str else count

def getWordLength(str, ord = True):
  wordLen = 0
  ch = str[0] if ord else str[-1]
  for i in str if ord else str[::-1]:
    if ch != i: break
    else: wordLen += 1
  return wordLen

def whoWins(string: str):
  turn = 0
  if '?' in string:
    if string == "?":
      return 0
    elif string[0] == '?':
      if countWords(string[1:])%2 == 0:
        string = string[1] + string[1:]
      else:
        string = 0 if string[1] == 1 else 1 + string[1:]
    elif string[-1] == '?':
      if countWords(string[:-1])%2 == 0:
        string = string[:-2] + string[-2]
      else:
        string = string[:-2] + 0 if string[-2] == 1 else 1
    else:
      string.replace('?', '0')
  turn += 1
  
  while countWords(string) == 1:
    fword = getWordLength(string)
    lword = getWordLength(string, False)
    if fword > 1:
      string = string[fword-(countWords(string)%2-1):]
    elif lword > 1:
      string = string[:-(lword-(countWords(string)%2-1))]
    else:
      string = string [1:]
    turn += 1
  return turn%2

string = sys.stdin.readline().strip()
print(whoWins(string))


# 문자 ?의 처리

# 문자 ?의 앞뒤가 다른 경우
# 0?1 -> 001, 011 -> 2번

# 문자 ?의 앞뒤가 같은 경우
# 0?0 -> 000, 010 -> 1, 3번

# 문자 ?가 중간에 위치 할 경우 문자?를 생략 했을경우와 차이가 없다.
# 0?1 -> 01, 0?0 -> 00 둘 다 홀수 짝수로 같은 결과 도출
# 따라서 문자 ?를 제거하고 단어의 갯수를 세어 +1만큼 턴을 반복

# 문자 ?가 문자열의 맨 앞 또는 뒤에 위치 할 경우
# 맨 뒤 0? -> 00, 01 -> 1, 2번
# 맨 앞 ?1 -> 11, 01 -> 1, 2번

# 문자 ?를 제거했을때보다 1번의 추가 행동이 생길 가능성 있음
# 처음부터 문자열 앞 또는 끝에 ?가 오지 않는 이상 이길 수 있는 순번에 있는 사람이 ?를 먼저 제거함
# 따라서 문자열 중간에 낀 ?가 앞뒤 단어를 지운다고 끝으로 올 가능성은 배제 가능
# 처음부터 문자열 가장자리에 오는 경우는 무조건 시작하는 사람이 승리 -> 준범

# 문자 ? 혼자 오는 경우
# 0, 1로 변경 후 지우는 사람 즉 2번째 사람이 승리 -> 명섭

# 문자 ? 가 나오지 않는 경우
# 단어의 갯수만큼 턴을 반복

# 가장 앞 또는 뒤의 연속된 같은 숫자 1개 이상 지우는 경우의 처리
# 001 -> 01, 1 -> 2, 1번
# 0001 -> 001, 01, 1 -> ?, 2, 1번
# 결국 지는 모양: 01, 10
# 01, 10을 만들면 이김 -> 01, 10이 아닌 단어 2개 남은 상황이 오면 이김
# ex) 00011, 1110, 000000001111, ...
# 100011, 000110, 
# 1011100?1010001
# 101110001010001
#  01110001010001
#   1110001010001
#      0001010001 - 01010001로 만들면 승리 가능
#         1010001 승리 확정
#          010001 패배 확정
#           10001 승리 확정
#            0001
#               1
# 짐

# 남은 모양을 무조건 짝수개의 단어로 만들기