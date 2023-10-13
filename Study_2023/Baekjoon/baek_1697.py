import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
dist = [0 for _ in range(10 ** 5 +1)]

def bfs(x):
    q = deque([x])
    while q:
        x = q.popleft()
        if x == k:
            return dist[x]
        for i in (x-1, x+1, x*2):
            if 0 <= i < 10**5 + 1 and not dist[i]:
               dist[i] = dist[x] + 1
               q.append(i)

print(bfs(n))


