import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited = [[0] * m for _ in range(n)]
    visited[i][j] = 1
    count = 0
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            elif graph[nx][ny] == 'L' and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                count = max(count, visited[nx][ny])
                q.append((nx, ny))
    return count - 1

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            result = max(result, bfs(i, j))
print(result)