import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(arr, n, m):
    q = deque()
    q.append((0,0))
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True
    count = 0
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if arr[nx][ny] == 0:
                    # 치즈가 아닌 부분만 queue에 담음(가장자리만 체크)
                    q.append((nx, ny))
                else: # 1을 만나면
                    arr[nx][ny] = 0    # 치즈 녹임 -> 0으로 만듦
                    # 공기 접촉 X -> queue에 넣지 않음, count만 1 증가
                    count += 1
                visited[nx][ny] = True
    
    return count

def solution(n, m , arr):
    time = 0
    while True:
        time += 1
        count = bfs(arr, n, m)    # 단계마다 녹은 치즈 갯수
        result.append(count)      # 각 단계별 녹은 치즈 수 추가
        if count == 0:  # 치즈 X -> 멈춤
            break
    return time - 1, result[-2] if len(result) > 1 else 0

time, count = solution(n, m, arr)
print(time)
print(count)
                  
