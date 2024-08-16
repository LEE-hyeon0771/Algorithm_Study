import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(input().rstrip()))

visited = [[False]*m for _ in range(n)]
dp = [[-1] * m for _ in range(n)]

result = 0
def dfs(x, y, count):
    if x < 0 or y < 0 or x >= n or y >= m or board[x][y] == 'H':
        return count - 1
    if visited[x][y]:
        return -1
    if dp[x][y] != -1:
        return count + dp[x][y]
    
    visited[x][y] = True
    num = int(board[x][y])
    
    result = count
    
    for dx, dy in directions:
        nx = x + dx*num
        ny = y + dy*num
        temp = dfs(nx, ny, count + 1)
        if temp == -1:
            return -1
        result = max(result, temp)
    visited[x][y] = False
    dp[x][y] = result - count
    return result

answer = dfs(0, 0, 1)
if answer != -1:
    print(answer)
else:
    print(-1)