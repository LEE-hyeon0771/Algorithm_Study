import sys
import math
input = sys.stdin.readline

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX < rootY:
            self.parent[rootY] = rootX
        else:
            self.parent[rootX] = rootY

n, m = map(int, input().split())
nodes = [tuple(map(int, input().split())) for _ in range(n)]
disjoint_set = DisjointSet(n)
edges = []

for _ in range(m):
    a, b = map(int, input().split())
    disjoint_set.union(a, b)

for i in range(n):
    for j in range(i + 1, n):
        cost = math.sqrt((nodes[i][0] - nodes[j][0]) ** 2 + (nodes[i][1] - nodes[j][1]) ** 2)
        edges.append((cost, i + 1, j + 1))

total_cost = 0
for cost, node1, node2 in sorted(edges):
    if disjoint_set.find(node1) != disjoint_set.find(node2):
        disjoint_set.union(node1, node2)
        total_cost += cost

print(f"{total_cost:.2f}")