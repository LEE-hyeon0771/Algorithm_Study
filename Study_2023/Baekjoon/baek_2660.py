import sys
from collections import deque
from collections import defaultdict

input = sys.stdin.readline

q = deque()
n = int(input())
graph = [[] for _ in range(n+1)]
while True:
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    if a == -1 and b == -1:
        break

def bfs(s):
    visited[s] = 1
    q.append(s)
    while q:
        u = q.popleft()
        for v in graph[u]:
            if not visited[v]:
                q.append(v)
                dist[v] = dist[u] + 1
                visited[v] = 1

result = defaultdict(int)
for i in range(1, n+1):
    dist = [0 for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    visited[i] = 1
    bfs(i)
    max_dist = max(dist)
    result[i] = max_dist

min_dist = min(result.values())
candidate = []
for i, dist in result.items():
    if dist == min_dist:
        candidate.append(i)

print(min_dist, len(candidate))
print(*candidate)



