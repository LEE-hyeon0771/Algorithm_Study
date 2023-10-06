import sys

input = sys.stdin.readline

n = int(input())
height = []
stack = []
for i in range(n):
    height.append(int(input()))

result = 0
for i in height:
    while stack and stack[len(stack) - 1] <= i:
        stack.pop()
    stack.append(i)
    result += len(stack) - 1

print(result)