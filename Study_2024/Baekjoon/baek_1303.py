from collections import deque

n, m = map(int, input().split())
graph = [list(input()) for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False for _ in range(n)]for _ in range(m)]


def bfs(x, y, c):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == c and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    count += 1
    
    return count

w = 0
b = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 'W' and not visited[i][j]:
            w += bfs(i, j, 'W') ** 2
        elif graph[i][j] == 'B' and not visited[i][j]:
            b += bfs(i, j, 'B') ** 2

print(w, b)
