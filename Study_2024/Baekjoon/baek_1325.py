import sys
input = sys.stdin.readline
from collections import deque

def find_computers_to_hack(N, trust_relations):
    graph = [[] for _ in range(N + 1)]
    for a, b in trust_relations:
        graph[b].append(a)
    def bfs(start):
        visited = [False] * (N + 1)
        queue = deque([start])
        visited[start] = True
        count = 0
        while queue:
            current = queue.popleft()
            count += 1
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return count

    max_hack = 0
    result = []
    for i in range(1, N + 1):
        hacked = bfs(i)
        if hacked > max_hack:
            max_hack = hacked
            result = [i]
        elif hacked == max_hack:
            result.append(i)
    
    return result
N, M = map(int, input().split())
trust_relations = [tuple(map(int, input().split())) for _ in range(M)]
result = find_computers_to_hack(N, trust_relations)
print(*result)