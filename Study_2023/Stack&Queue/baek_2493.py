import sys
input = sys.stdin.readline
N = int(input())
tower = list(map(int, input().split()))

result = []
stack = []

for i in range(N):
    while stack:
        if tower[stack[-1][0]] < tower[i]:     # 수신 X
            stack.pop()
        else:
            result.append(stack[-1][0] + 1)    # 수신 O
            break
    if not stack:
        result.append(0)
    stack.append([i, tower[i]])
print(" ".join(map(str, result)))
