import sys

N = int(sys.stdin.readline())

words = [sys.stdin.readline().strip() for _ in range(N)]

words = list(set(words))
words.sort(key=lambda x: (len(x), x))

print(*words, sep='\n')