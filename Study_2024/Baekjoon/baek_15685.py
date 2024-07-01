'''
초기 방향을 리스트 저장
현재 커브 방향 리스트를 반대로 뒤집고 각 방향에 1을 더해서 새로운 방향 리스트 만듦
1세대 : 0 1

2세대 : 0 1 2 1

3세대 : 0 1 2 1 2 3 2 1

4세대 : 0 1 2 1 2 3 2 1 2 3 0 3 2 3 2 1
'''

import sys
input = sys.stdin.readline

directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def generate_dragon_curve(x, y, d, g):
    curve = [d]
    for _ in range(g):
        curve += [(i+1) % 4 for i in reversed(curve)]

    points = [(x, y)]      # 시작점
    for direction in curve:
        x, y = x + directions[direction][0], y + directions[direction][1]
        points.append((x, y))
    return points

n = int(input())
curves = []
for _ in range(n):
    x, y, d, g = map(int, input().split())
    curves.append((x, y, d, g))

# 격자 표시 100*100 격자
grid = [[False] * 101 for _ in range(101)]

for x, y, d, g in curves:
    points = generate_dragon_curve(x, y, d, g)
    for px, py in points:
        if 0 <= px <= 100 and 0 <= py <= 100:
            grid[px][py] = True

# 1*1 정사각형 꼭짓점 카운팅
count = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] and grid[i+1][j] and grid[i][j+1] and grid[i+1][j+1]:
            count += 1

print(count)