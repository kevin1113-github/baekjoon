import sys

x, y = map(int, sys.stdin.readline().split())
days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(days[(sum(months[:x - 1]) + y) % 7])
