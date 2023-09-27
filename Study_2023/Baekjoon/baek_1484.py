import sys

input = sys.stdin.readline

G = int(input().rstrip())

result = []
first = 1
second = 1

while True:

    temp = first**2 - second**2
    if 2 > first - second >= 1 and temp > G:
        break
    if temp < G:
        first += 1
    elif temp > G:
        second += 1
    else:
        result.append(first)
        first += 1

if result:
    print(*result, sep='\n')
else:
    print(-1)

