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
from collections import deque

def calculate_min_cost(n, c):
    initial_state = tuple([1] * n)
    dp = {initial_state: 0}
    queue = deque([initial_state])

    while queue:
        v = queue.popleft()
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                u = list(v)
                u[i] += v[j]
                u.pop(j)
                u = tuple(sorted(u))
                new_cost = dp[v] + v[i] * v[j] * (1 - c[n - len(v)])
                
                if u not in dp or dp[u] > new_cost:
                    dp[u] = new_cost
                    queue.append(u)

    return dp[(n,)]

n = int(input())
c = list(map(int, input().split()))

result = calculate_min_cost(n, c)
print(result)