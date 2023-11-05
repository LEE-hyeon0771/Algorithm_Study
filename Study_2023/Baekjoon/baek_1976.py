import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
parent = [i for i in range(n)]
arr = [list(map(int, input().split())) for _ in range(n)]
path_check = list(map(int, input().split()))

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

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            union(parent, i, j)

for i in range(1, m):
    if parent[path_check[i] - 1] != parent[path_check[0] - 1]:
        print("NO")
        break
else:
    print("YES")


