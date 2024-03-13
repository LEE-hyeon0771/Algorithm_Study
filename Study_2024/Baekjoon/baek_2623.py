import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
orders = []

for i in range(m):
    order = list(map(int, input().split()))
    orders.append(order)
    
def sorting(n, orders):   
    graph = [[] for _ in range(n+1)]
    in_Degree = [0 for _ in range(n+1)]
    
    for order in orders:
        for i in range(1, len(order) - 1):
            graph[order[i]].append(order[i+1])
            in_Degree[order[i+1]] += 1
            
    q = deque()
    for i in range(1, n+1):
        if in_Degree[i] == 0:
            q.append(i)

    result = []
    while q:
        curr = q.popleft()
        result.append(curr)
        for i in graph[curr]:
            in_Degree[i] -= 1
            if in_Degree[i] == 0:
                q.append(i)
    
    if len(result) != n:
        return [0]
    else:
        return result

result = sorting(n, orders)
for i in result:
    print(i)
    