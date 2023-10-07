import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
first = int(input())
graph = [[] for _ in range(n+1)]
dist = [1e9] * (n+1)

for i in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(first):
    queue = []
    heapq.heappush(queue, (0, first))
    dist[first] = 0
    while queue:
        new_dist, curr = heapq.heappop(queue)
        if dist[curr] < new_dist:
            continue
        for i in graph[curr]:
            cost = new_dist + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

dijkstra(first)

for i in range(1, n+1):
    if dist[i] == 1e9:
        dist[i] = "INF"
    print(dist[i])
