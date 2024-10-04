import sys

mapdata = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]

x, y = 1, 1

while True:
  if mapdata[x][y] == 2:
    mapdata[x][y] = 9
    break
  mapdata[x][y] = 9
  if mapdata[x][y+1] == 1 and mapdata[x+1][y] == 1:
    break
  if mapdata[x][y+1] != 1:
    y += 1
  else:
    x += 1
  
for i in range(10):
  for j in range(10):
    print(mapdata[i][j], end=' ')
  print()
