import sys
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(k):
    x, y = map(int, input().split())
    graph[x][y] = True

def floyd():
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = True

floyd()

s = int(input())
for _ in range(s):
    a, b = map(int, input().split())
    if graph[a][b] == True:
        print(-1)
    elif graph[b][a] == True:
        print(1)
    else:
        print(0)