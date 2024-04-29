'''
트리의 지름 : 노드에서 bfs를 통해 가장 멀리 있는 노드를 구한 후 
해당 노드에서 bfs를 한번 더 수행해서 가장 멀리 있는 노드를 구함.
'''

import sys
from collections import deque
input = sys.stdin.readline

v = int(input().rstrip())
graph = [[] for _ in range(v+1)]

for _ in range(v):
    info = list(map(int, input().split()))
    node = info[0]
    i = 1
    while info[i] != -1:
        graph[node].append((info[i], info[i + 1]))
        i += 2

def bfs(start_node):
    visited = [-1] * (v + 1) 
    queue = deque([start_node])
    visited[start_node] = 0
    max_distance = 0
    max_node = start_node

    while queue:
        current = queue.popleft()
        current_distance = visited[current]
        
        for (neighbor, weight) in graph[current]:
            if visited[neighbor] == -1:  
                visited[neighbor] = current_distance + weight
                queue.append(neighbor)
                if visited[neighbor] > max_distance:  
                    max_distance = visited[neighbor]
                    max_node = neighbor

    return max_distance, max_node

_, farthest_node = bfs(1)
tree_diameter, _ = bfs(farthest_node)
print(tree_diameter)