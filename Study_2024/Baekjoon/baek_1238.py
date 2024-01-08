import sys
input = sys.stdin.readline
import heapq
INF = sys.maxsize

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start) :
    q = []
    dist = [INF] * (n+1)
    heapq.heappush(q, (0, start))
    dist[start] = 0
    
    while q :
        distance, node = heapq.heappop(q)
        if distance > dist[node] :
            continue
        
        for n_index, n_cost in graph[node] :
            c = distance + n_cost
            if c < dist[n_index]:
                dist[n_index] = c
                heapq.heappush(q, (c, n_index))
    
    return dist

answer = [0] * (n+1)
for i in range(1, n+1):
    answer[i] += dijkstra(i)[x]
    answer[i] += dijkstra(x)[i]

print(max(answer))