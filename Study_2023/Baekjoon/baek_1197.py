import sys

input = sys.stdin.readline

v, e = map(int, input().split())
parent = [i for i in range(v+1)]

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edge = []
cost = 0

for i in range(e):
    a, b, c = map(int, input().split())
    edge.append((c, a, b))

edge.sort()

for i in range(e):
    c, a, b = edge[i]
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        cost += c

print(cost)