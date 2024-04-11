import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [list(input()) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == graph[x][y]:
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

# 적록색맹 ㄴㄴ
count = 0
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            count += 1

# 적록색명 ㅇㅇ -> R에 G 넣고 bfs 다시 ㄱㄱ
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

count1 = 0
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            count1 += 1

print(count, count1)
                    
    