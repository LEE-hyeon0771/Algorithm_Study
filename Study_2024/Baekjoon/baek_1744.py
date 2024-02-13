# 양수 : 내림차순, 음수 : 오름차순
# 1은 무조건 더하기
# 0은 음수와 곱하는 것이 유리하므로 음수 list에 담기
# 마지막 하나 남는건 더해주기

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