import sys
from collections import deque

input = sys.stdin.readline

a,b,c = map(int, input().split())

q = deque()
q.append((0,0))

visited = [[0]*201 for _ in range(201)]
visited[0][0] = 1
answer = []

def xy_visit(x,y):
    if not visited[x][y]:
        visited[x][y] = 1
        q.append((x,y))

def bfs():
    while q:
        x, y = q.popleft()
        z = c - x - y

        if x == 0:
            answer.append(z)

        water = min(x, b-y)
        xy_visit(x-water, y+water)

        water = min(x, c-z)
        xy_visit(x-water, y)

        water = min(y, a-x)
        xy_visit(x+water, y-water)

        water = min(y, c-z)
        xy_visit(x, y-water)

        water = min(z, a-x)
        xy_visit(x+water, y)

        water = min(z, b-y)
        xy_visit(x, y+water)

bfs()
answer.sort()
print(*answer)