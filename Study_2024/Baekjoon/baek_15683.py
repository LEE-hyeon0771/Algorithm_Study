import sys
input = sys.stdin.readline
import copy

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
CCTV_DIRECTIONS = [
    [],
    [[0],[1],[2],[3]],
    [[0,2], [1,3]],
    [[0,1],[1,2],[2,3],[3,0]],
    [[0,1,3],[0,1,2],[1,2,3],[0,2,3]],
    [[0,1,2,3]]
]

def watch(x, y, direction, office):
    n, m = len(office), len(office[0])
    while True:
        x += DIRECTIONS[direction][0]
        y += DIRECTIONS[direction][1]
        if x < 0 or x >= n or y < 0 or y >= m or office[x][y] == 6:
            break
        if office[x][y] == 0:
            office[x][y] = '#'

def simulate(cctvs, idx, office):
    if idx == len(cctvs):
        return sum(row.count(0) for row in office)
    x, y, cctv_type = cctvs[idx]
    min_blind_spot = float('inf')
    
    for directions in CCTV_DIRECTIONS[cctv_type]:
        new_office = copy.deepcopy(office)
        for direction in directions:
            watch(x, y, direction, new_office)
        min_blind_spot = min(min_blind_spot, simulate(cctvs, idx + 1, new_office))
    return min_blind_spot

n, m = map(int, input().strip().split())
office = []
cctvs = []

for i in range(n):
    row = list(map(int, input().strip().split()))
    office.append(row)
    for j in range(m):
        if 1 <= row[j] <= 5:
            cctvs.append((i, j, row[j]))

min_blind_spot = simulate(cctvs, 0, office)
print(min_blind_spot)