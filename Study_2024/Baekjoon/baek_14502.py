import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations
from copy import deepcopy

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(temp):
    q = deque()
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                q.append((i, j))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    q.append((nx, ny))

def count_safe_area(temp):
    count = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                count += 1
    return count

empty_spaces = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 0]

max_safe_area = 0
for walls in combinations(empty_spaces, 3):        # 새로 세울 수 있는 벽 3개 조합.
    temp = deepcopy(graph)                         # 조합을 독립적으로 조절하기 위해서 deepcopy 시켜줌.
    
    for x, y in walls:
        temp[x][y] = 1
    
    # 바이러스 퍼트리기
    bfs(temp) 
    safe_area = count_safe_area(temp)
    max_safe_area = max(max_safe_area, safe_area)

print(max_safe_area)
