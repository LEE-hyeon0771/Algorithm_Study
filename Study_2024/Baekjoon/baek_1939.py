import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

island1, island2 = map(int, input().split())

def bfs(w):
    q = deque()
    visited = [False for _ in range(n+1)]
    visited[island1] = True
    q.append(island1)
    
    while q:
        x = q.popleft()
        
        # 끝에 도달하면 True
        if x == island2:
            return True
        
        # 방문하지 않았거나 무게가 w 이상인 경우를 queue에 담아줌
        for i, j in graph[x]:
            if not visited[i] and j >= w:
                visited[i] = True
                q.append(i)
    
    return False

result = 0
first = 1
end = sys.maxsize
while first <= end:
    mid = (first + end) // 2
    if bfs(mid):
        result = mid
        first = mid + 1
    else:
        end = mid - 1

print(result)
    