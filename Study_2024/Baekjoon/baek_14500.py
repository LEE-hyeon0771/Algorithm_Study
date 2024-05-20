import sys
input = sys.stdin.readline

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# 최대값 변수
maxValue = 0

# ㅗ, ㅜ, ㅓ, ㅏ 제외한 모양들 최대값 계산
def dfs(x, y, total, depth):
    global maxValue
    if depth == 4:
        maxValue = max(maxValue, total)
        return

    for i in range(4):
        nx = x + move[i][0]
        ny = y + move[i][1]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, total + board[nx][ny], depth + 1)
            visited[nx][ny] = False

# ㅗ, ㅜ, ㅓ, ㅏ 모양의 최대값 계산
def check_exception(x, y):
    global maxValue
    for i in range(4):
        tmp = board[x][y]
        for j in range(3):
            t = (i + j) % 4
            nx = x + move[t][0]
            ny = y + move[t][1]
            if not (0 <= nx < N and 0 <= ny < M):
                tmp = 0
                break
            tmp += board[nx][ny]
        maxValue = max(maxValue, tmp)
        

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, board[i][j], 1)
        visited[i][j] = False
        check_exception(i, j)

print(maxValue)