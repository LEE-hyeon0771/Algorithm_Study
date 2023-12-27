import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
alpha = [0] * 26
alpha[ord(board[0][0]) - ord('A')] = True
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
max_count = 0

def dfs(x, y, cnt):
    global max_count
    max_count = max(max_count, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if (alpha[ord(board[nx][ny]) - ord('A')]) == False:
                alpha[ord(board[nx][ny]) - ord('A')] = True
                dfs(nx, ny, cnt + 1)
                alpha[ord(board[nx][ny]) - ord('A')] = False

dfs(0, 0, 1)
print(max_count)