import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]

shark_size = 2
shark_x, shark_y = 0, 0
for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            shark_x = i
            shark_y = j
            space[i][j] = 0
            
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited = [[-1]*n for _ in range(n)]
    visited[x][y] = 0
    q = deque([(x, y)])
    fish = []
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == -1 and space[x][y] <= shark_size:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                    if 0 < space[nx][ny] < shark_size:
                        fish.append((visited[nx][ny], nx, ny))
    
    return sorted(fish, key=lambda x: (x[0], x[1], x[2]))

time = 0
eat = 0

while True:
    fish = bfs(shark_x, shark_y)
    if not fish:
        break
    
    # 가장 가까운 물고기 냠
    dist, nx, ny = fish[0]
    time += dist
    eat += 1
    # 먹었으면 빈칸으로
    space[nx][ny] = 0
    
    if eat == shark_size:
        shark_size += 1
        eat = 0
        
    shark_x = nx
    shark_y = ny

print(time)
                    