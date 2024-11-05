# import sys

# scores = [int(sys.stdin.readline()) for _ in range(5)]

# total_score = 0
# for i in range(5):
#   total_score += scores[i] if scores[i] >= 40 else 40

# print(total_score // 5)

print(sum(map(lambda x: x if x >= 40 else 40, [int(input()) for _ in range(5)]))//5)
