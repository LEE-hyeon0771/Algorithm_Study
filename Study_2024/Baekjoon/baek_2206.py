# 방문 안해 : 0, 방문해 : 1
# broken이 0 이면 벽을 부수지 않은 상태
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(n, m, graph):
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
    q = deque([(0,0,0,1)])      # (x, y, 벽을 부쉈는지 여부, 현재까지의 거리)
    visited[0][0][0] = True
    
    while q:
        x, y, broken, dist = q.popleft()
        
        if x == n-1 and y == m-1:
            return dist
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                # 벽이 없는 곳으로 이동하는 경우
                if graph[nx][ny] == 0 and not visited[nx][ny][broken]:
                    visited[nx][ny][broken] = True
                    q.append((nx, ny, broken, dist + 1))
                # 벽이 있는 곳으로 이동하는 경우 (벽을 한 번도 부순 적이 없는 경우)
                elif graph[nx][ny] == 1 and broken == 0 and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    q.append((nx, ny, 1, dist + 1))
                    
    return -1
    
print(bfs(n, m, graph))
    