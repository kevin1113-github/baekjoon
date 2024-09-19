import sys

S = sys.stdin.readline()

total_set = set()

for start in range(len(S)):
  for end in range(start, len(S)):
    total_set.add(S[start:end])

print(len(total_set)-1)
