import sys
input = sys.stdin.readline

n = int(input())
positive = []
negative = []
ones = 0
result = 0
for i in range(n):
    num = int(input())
    if num > 1:
        positive.append(num)
    elif num <= 0:
        negative.append(num)
    elif num == 1:
        ones += 1
    else:
        result += num

positive.sort(reverse=True)
negative.sort()

for i in range(0, len(positive)-1, 2):
        result += positive[i] * positive[i+1]
if len(positive) % 2 == 1:
        result += positive[-1]

for i in range(0, len(negative)-1, 2):
        result += negative[i] * negative[i+1]
if len(negative) % 2 == 1:
        result += negative[-1]

result += ones
print(result)