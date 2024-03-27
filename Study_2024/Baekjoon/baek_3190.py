# maps[y][x] = 0 초기값
# maps[y][x] = 1 뱀 차지 칸
# maps[y][x] = 2 사과 있는 칸

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
k = int(input())
maps = [[0] * (n+1) for _ in range(n+1)]
for i in range(k):
    x, y = map(int, input().split())
    maps[x][y] = 2 # 사과 위치

# 방향 정보
direction_changes = {}
m = int(input())
for _ in range(m):
    x, c = input().split()
    direction_changes[int(x)] = c

time = 0
directions = [(0,1), (1,0), (0,-1), (-1,0)]
direction_index = 0
x = 1
y = 1
maps[y][x] = 1   # 뱀 초기 위치
snakes_move = deque([(y,x)])

while True:
    time += 1
    ny, nx = y + directions[direction_index][0], x + directions[direction_index][1]
    
    # 벽 또는 자기 자신 몸과 부딪히는지
    if 1 <= ny <= n and 1 <= nx <= n and maps[ny][nx] != 1:
        if maps[ny][nx] == 2:    # 사과 있으면 사과 없애고 꼬리 그대로
            maps[ny][nx] = 1     
            snakes_move.append((ny, nx))
        
        #사과 없으면, 몸길이 줄여 꼬리 위치 칸 비워줌
        else:
            maps[ny][nx] = 1
            snakes_move.append((ny, nx))
            ty, tx = snakes_move.popleft()
            maps[ty][tx] = 0
        y, x = ny, nx
    else:
        break   # 벽 또는 자기 몸과 부딪힘 -> break
    
    # direction_index = 3(북쪽), direction_index = 0(동쪽)
    # 반시계방향 회전 시 -1, 시계 방향 회전 시 +1
    if time in direction_changes:
        if direction_changes[time] == 'L':
            direction_index = (direction_index - 1) % 4
        else:
            direction_index = (direction_index + 1) % 4

print(time)