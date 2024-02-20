import sys
input = sys.stdin.readline
INF = sys.maxsize

n, d = map(int, input().split())
graph = [[] for _ in range(d+1)]
dist = [INF for _ in range(d+1)]

for i in range(d):
    graph[i].append((i+1, 1))

for _ in range(n):
    a, b, c = map(int, input().split())
    if b > d:
        continue
    graph[a].append((b, c))
    
def dijkstra(start):
    dist[start] = 0
    for now in range(d+1):
        for next_node, weight in graph[now]:
            if next_node <= d and dist[now] + weight < dist[next_node]:
                dist[next_node] = dist[now] + weight
 
dijkstra(0)
print(dist[d])