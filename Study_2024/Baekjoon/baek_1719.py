import sys
input = sys.stdin.readline
INF = sys.maxsize

def floyd_warshall(n, m, edges):
    INF = float('inf')
    graph = [[INF] * n for _ in range(n)]
    node = [[0] * n for _ in range(n)]

    for i in range(n):
        graph[i][i] = 0

    for x, y, z in edges:
        graph[x-1][y-1] = z
        graph[y-1][x-1] = z
        node[x-1][y-1] = y
        node[y-1][x-1] = x

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]         # 플로이드 워셜로 최솟값 갱신
                    node[i][j] = node[i][k]           # 새로운 집하장 k로 갱신

    return node


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
path_table = floyd_warshall(n, m, edges)

for i in range(n):
    for j in range(n):
        if path_table[i][j] == 0:
            print('-', end=' ')
        else:
            print(path_table[i][j], end=' ')
    print()