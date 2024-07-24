import sys
input = sys.stdin.readline

def find(x):
    if parent[x] < 0:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    parent[y] = x


G = int(input())
P = int(input())
parent = [-1 for i in range(G+1)]
result = 0
for i in range(P):
    g = int(input())
    target = find(g)
    if target == 0:
        break
    union(target-1, target)
    result += 1

print(result)