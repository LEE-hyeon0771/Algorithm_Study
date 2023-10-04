import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(input().rstrip())
alpha = {}

for i in arr:
    length = len(i)-1
    for j in i:
        if j not in alpha:
            alpha[j] = 10**length
        else:
            alpha[j] += 10**length
        length -= 1

alpha = sorted(alpha.values(), reverse=True)
result = 0
num = 9
for i in alpha:
    result += i * num
    num -= 1
print(result)
