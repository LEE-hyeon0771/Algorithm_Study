import sys
import heapq
maxsize = int(1e9)
input = sys.stdin.readline

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

def dijkstra(graph, start):
    distances = [maxsize] * (n+1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination]:
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])

    return distances

v1, v2 = map(int, input().split())
result = dijkstra(graph, 1)
v1_result = dijkstra(graph, v1)
v2_result = dijkstra(graph, v2)

v1_answer = result[v1] + v1_result[v2] + v2_result[n]
v2_answer = result[v2] + v1_result[n] + v2_result[v1]

min_answer = min(v1_answer, v2_answer)

if min_answer < maxsize:
    print(min_answer)
else:
    print(-1)
