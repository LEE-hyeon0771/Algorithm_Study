import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)
n, m, k = map(int, input().split())
graph = [[0]*(m+1) for _ in range(n+1)]
visited = [[0]*(m+1) for _ in range(n+1)]

for i in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(graph, visited, x, y):
    global count
    visited[x][y] = count
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and graph[nx][ny]:
                count += 1
                dfs(graph, visited, nx, ny)
            
max_count = 0     
for i in range(n+1):
    for j in range(m+1):
        if graph[i][j] and not visited[i][j]:
            count = 1
            dfs(graph, visited, i, j)
            max_count = max(max_count, count)
            
print(max_count)
    