import sys
input = sys.stdin.readline
from collections import deque
n, k = map(int, input().split())

def bfs(n, k):
    visited = [False] * 100001
    
    q = deque([(n, 0)])
    visited[n] = True
    
    while q:
        x, t = q.popleft()
        
        if x == k:
            return t
        
        for nx in [x - 1, x + 1, 2*x]:
            if 0 <= nx <= 100000 and not visited[nx]:
                visited[nx] = True
                if nx == 2*x:         # 순간이동 -> t 그대로
                    q.appendleft((nx, t))
                else:
                    q.append((nx, t+1))
    
    return -1

print(bfs(n, k))