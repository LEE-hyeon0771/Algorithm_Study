import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
result = [-1] * n
stack = []

for i in range(n):
    while stack and a[stack[-1]] < a[i]:
        result[stack[-1]] = a[i]
        stack.pop()
    stack.append(i)

print(*result)

