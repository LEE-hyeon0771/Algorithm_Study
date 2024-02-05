import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1
    
    # if not visited
    if dp[x][y] == -1:
        dp[x][y] = 0         # visited 처리
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 새로 찾은 (nx, ny)가 (x, y)의 값보다 작다면 dfs 다시 불러서 갯수 더해주기
                if graph[nx][ny] < graph[x][y]:
                    dp[x][y] += dfs(nx, ny)
    
    return dp[x][y]

print(dfs(0, 0))
