# 대각선에 있거나, 같은 행에 퀸 존재 -> 퀸 놓기 X
# 퀸 놓기 불가 시 다음 탐색
import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * n

def check(x):
    for i in range(x):
        if arr[x] == arr[i] or abs(arr[x] - arr[i]) == abs(x-i):
            return False
    return True

def dfs(x):
    global answer
    
    if x == n:
        answer += 1
    else:
        for i in range(n):
            arr[x] = i
            if check(x):
                dfs(x + 1)

answer = 0
dfs(0)
print(answer)