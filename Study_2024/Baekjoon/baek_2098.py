'''
last_city가 방문되지 않았다면 스킵
next_city가 이미 방문되었거나 갈 수 없으면 스킵
모든 도시 방문 상태에서 시작 도시로 돌아오는 비용을 계산'''
import sys
input = sys.stdin.readline

def tsp(n, w):
    INF = float('inf')
    dp = [[INF]*n for _ in range(1 << n)]
    
    dp[1][0] = 0
    
    for visited in range(1 << n):
        for last_city in range(n):
            if visited & (1 << last_city) == 0:
                continue
            for next_city in range(n):
                if visited & (1 << next_city) != 0 or w[last_city][next_city] == 0:
                    continue
                # visited 상태에서 next_city를 추가로 방문하도록 추가, 값을 min으로 갱신
                next_visited = visited | (1 << next_city)
                dp[next_visited][next_city] = min(dp[next_visited][next_city], dp[visited][last_city] + w[last_city][next_city])
                
        min_cost = INF
        for last_city in range(1, n):
            if w[last_city][0] != 0:
                min_cost = min(min_cost, dp[(1 << n) - 1][last_city] + w[last_city][0])
        
    return min_cost
    
n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
    
print(tsp(n, w))