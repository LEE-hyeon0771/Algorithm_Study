'''import sys
input = sys.stdin.readline
import heapq
INF = sys.maxsize

v, e = map(int, input().split())
arr = [[] for _ in range(v+1)]
distance = [[INF] * (v + 1) for _ in range(v + 1)]
heap = []

# dist, 위치1, 위치2 순서로 heap에 push
for _ in range(e):
    a, b, c = map(int, input().split())
    arr[a].append([c, b])
    heapq.heappush(heap, [c, a, b])

while heap:
    dist, first, last = heapq.heappop(heap)
    if first == last:
        print(dist)
        break

    if distance[first][last] < dist:
        continue

    for i, j in arr[last]:
        # first -> last -> j
        n_distance = i + dist
        # (first->last->j vs first -> j) if more cheap, change n_distance
        if distance[first][j] > n_distance:
            distance[first][j] = n_distance
            heapq.heappush(heap, [distance[first][j], first, j])
'''

import sys
input = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, input().split())
distance = [[INF] * (v + 1) for _ in range(v + 1)]
for i in range(1, v+1):
    distance[i][i] = INF

for _ in range(e):
    a, b, c = map(int, input().split())
    distance[a][b] = c

for i in range(1, v+1):
    for j in range(1, v+1):
        for k in range(1, v+1):
            distance[j][k] = min(distance[j][k], distance[j][i] + distance[i][k])


result = min(distance[i][i] for i in range(1, v+1))

if result == INF:
    print(-1)
else:
    print(result)
