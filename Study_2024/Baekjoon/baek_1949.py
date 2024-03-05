# dp[v][0] : 마을 v가 우수마을 X -> v와 자손 노드들로부터 얻을 수 있는 최대 주민 수
# dp[v][1] : 마을 v가 우수마을 O -> v와 자손 노드들로부터 얻을 수 있는 최대 주민 수
# v가 우수마을 X -> 자식 u는 우수마을 or 우수마을 X 모두 가능
# v가 우수마을 O -> 자식 u는 우수마을 X
# 우수마을 선정 시 + 우수마을 선정 X 시의 최대 주민 수 비교해서 max 값

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n = int(input())
population = list(map(int, input().split()))
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dp = [[0, 0] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

def dfs(v):
    visited[v] = True
    dp[v][0] = 0
    dp[v][1] = population[v-1]
    for u in tree[v]:
        if not visited[u]:
            dfs(u)
            dp[v][0] += max(dp[u][0], dp[u][1])   # v가 우수마을이 아닐 때
            dp[v][1] += dp[u][0] # v가 우수마을이 일 때

dfs(1) # 루트노드(1번 마을)
print(max(dp[1][0], dp[1][1]))           