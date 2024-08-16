import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]
    dp[x][y] = 1
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n and forest[x][y] < forest[nx][ny]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    
    return dp[x][y]

result = 0
for i in range(n):
    for j in range(n):
        result = max(result, dfs(i, j))

print(result)