import sys
input = sys.stdin.readline
from collections import deque

def escape_maze(R, C, maze):
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    fire_queue = deque()
    jihun_queue = deque()
    fire_time = [[-1]*C for _ in range(R)]
    jihun_time = [[-1]*C for _ in range(R)]
    
    for r in range(R):
        for c in range(C):
            if maze[r][c] == 'F':
                fire_queue.append((r, c))
                fire_time[r][c] = 0
            elif maze[r][c] == 'J':
                jihun_queue.append((r, c))
                jihun_time[r][c] = 0
    
    while fire_queue:
        x, y = fire_queue.popleft()
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < R and 0 <= ny < C and maze[nx][ny] == '.' and fire_time[nx][ny] == -1:
                fire_time[nx][ny] = fire_time[x][y] + 1
                fire_queue.append((nx, ny))
                
    while jihun_queue:
        x, y = jihun_queue.popleft()
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < R and 0 <= ny < C:
                if maze[nx][ny] == '.' and jihun_time[nx][ny] == -1:
                    if fire_time[nx][ny] == -1 or jihun_time[x][y] + 1 < fire_time[nx][ny]:
                        jihun_time[nx][ny] = jihun_time[x][y] + 1
                        jihun_queue.append((nx, ny))
            else:
                return jihun_time[x][y] + 1
    
    return "IMPOSSIBLE"

R, C = map(int, input().split())
maze = [input() for _ in range(R)]

print(escape_maze(R, C, maze))