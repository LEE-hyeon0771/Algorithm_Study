import sys

input = sys.stdin.readline

n = int(input())

point = []
for i in range(n):
    point.append(list(map(int, input().split())))

point.append(point[0])
x = 0
y = 0

for i in range(n):
    x += point[i][0] * point[i+1][1]
    y += point[i][1] * point[i+1][0]

answer = abs(x-y) / 2

print(answer)