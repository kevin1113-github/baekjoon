import sys

def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a % b)

def get_distances(X):
  distances = [X[i] - X[i - 1] for i in range(1, len(X))]
  return distances

def get_gcds(distances):
  _gcd = distances[0]
  for distance in distances[1:]:
    _gcd = gcd(_gcd, distance)
  return _gcd

def count_trees(distances, gcd):
  count = 0
  for distance in distances:
    count += distance // gcd - 1
  return count

N = int(sys.stdin.readline())

X = [int(sys.stdin.readline()) for _ in range(N)]

distances = get_distances(X)
_gcd = get_gcds(distances)
count = count_trees(distances, _gcd)

print(count)
