import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
cost = [[-1 for _ in range(m)] for _ in range(n)]

da = [-1, 1, 0, 0]
db = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    cost[x][y] = 0

    while q:
        a, b = q.popleft()
        for i in range(4):
            new_a = a + da[i]
            new_b = b + db[i]

            if 0 <= new_a < n and 0 <= new_b < m and cost[new_a][new_b] == -1:
                if arr[new_a][new_b] == 0:
                    cost[new_a][new_b] = cost[a][b]
                    q.appendleft((new_a, new_b))
                else:
                    cost[new_a][new_b] = cost[a][b] + 1
                    q.append((new_a, new_b))
    print(cost[n - 1][m - 1])

bfs(0,0)




