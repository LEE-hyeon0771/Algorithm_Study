import sys

input = sys.stdin.readline

n, h = map(int, input().split())

seok = [0] * (h+1)
jong = [0] * (h+1)
total = [0] * (h+1)
for i in range(n):
    num = int(input())
    if i % 2 == 0:
        seok[h - num + 1] += 1
    else:
        jong[num] += 1

for i in range(h-1, 0, -1):
    jong[i] += jong[i+1]

for i in range(1, h+1):
    seok[i] += seok[i-1]

for i in range(1, h+1):
    total[i] = seok[i] + jong[i]
total.pop(0)
print(min(total), total.count(min(total)))

