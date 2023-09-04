import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, finish):
    q = deque()
    q.append((start, 0))
    visited = [0] * (N+1)
    visited[start] = 1
    while q:
        v, w = q.popleft()
        if v == finish:
            return w
        for i, j in arr[v]:
            if not visited[i]:
                visited[i] = 1
                q.append((i, j + w))


N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]

for _ in range(N-1):
    a,b,c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

for _ in range(M):
    d, e = map(int, input().split())
    print(bfs(d, e))