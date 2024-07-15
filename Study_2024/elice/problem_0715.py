'''
빨간 선과 파란 선
제한 시간: 1 초
N개의 정점이 있다.
차례마다 다음을 반복해서 N개의 정점 사이에 간선을 연결하려고 한다.

먼저 2개의 서로 연결되지 않은 정점 u와 v를 고른다.
그 이후, u가 포함된 연결 요소의 모든 정점들 각각에서, v가 포함된 연결 요소의 모든 정점들 각각으로 간선을 추가한다.
간선의 색은 빨간색 혹은 파란색이다.
k번째 차례에 사용할 색깔이 주어질 때, 정점을 골라서 얻을 수 있는 빨간 간선 개수의 최솟값을 구하여라.


입력
첫 번째 줄에 정점의 수 N이 주어진다.
2≤N≤30
두 번째 줄에 각 차례에 사용할 색깔을 표시하는 N−1개의 수가 공백을 구분으로 주어진다.
숫자가 0이면 빨간 간선을, 1이면 파란 간선을 사용한다는 뜻이다.
입력되는 모든 수들은 정수이다.
출력
문제의 조건을 만족하면서 간선을 연결할 때, 얻을 수 있는 빨간 간선 개수의 최솟값을 출력한다.
입력 예시
5
1 1 0 1

출력 예시
1
'''
import sys
input = sys.stdin.readline
def min_red_edges(n, colors):
    parent = list(range(n))
    size = [1] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            if size[rootX] < size[rootY]:
                rootX, rootY = rootY, rootX
            parent[rootY] = rootX
            size[rootX] += size[rootY]

    red_edge_count = 0

    for i, color in enumerate(colors):
        possible_edges = []
        for a in range(n):
            for b in range(a + 1, n):
                if find(a) != find(b):
                    possible_edges.append((size[find(a)] * size[find(b)], a, b))
        
        
        possible_edges.sort()
        _, u, v = possible_edges[0]


        if color == 0:
            red_edge_count += 1

        union(u, v)

    return red_edge_count

n = int(input().strip())
colors = list(map(int, input().strip().split()))
print(min_red_edges(n, colors))