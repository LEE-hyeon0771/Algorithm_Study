import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
q = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append([i, j])

da = [-1, 1, 0, 0]
db = [0, 0, -1, 1]
def bfs():
    while q:
        a, b = q.popleft()
        for i in range(4):
            new_a = da[i] + a
            new_b = db[i] + b
            if 0 <= new_a < n and 0 <= new_b < m and arr[new_a][new_b] == 0:
                arr[new_a][new_b] = arr[a][b] + 1
                q.append([new_a, new_b])

bfs()
result = 0
is_break = False
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            print(-1)
            exit()
        result = max(result, arr[i][j])
        if arr[i][j] == 0:
            is_break = True
            break
    if is_break:
        break
print(result - 1)