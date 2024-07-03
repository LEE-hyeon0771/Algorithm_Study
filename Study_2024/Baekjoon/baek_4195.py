import sys
input = sys.stdin.readline

def union(x, y, parent, size):
    rootX = find(x, parent)
    rootY = find(y, parent)
    
    if rootX != rootY:
        parent[rootY] = rootX
        size[rootX] += size[rootY]

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

T = int(input())
results = []
for _ in range(T):
    F = int(input())
    parent = {}
    size = {}
    for _ in range(F):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            size[a] = 1
        if b not in parent:
            parent[b] = b
            size[b] = 1
        union(a, b, parent, size)
        results.append(size[find(a, parent)])
for result in results:
    print(result)