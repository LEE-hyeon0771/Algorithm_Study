# 현재 i명 모집 시 cost 비용 vs i명 확보하는데까지 계산된 최소 비용

import sys
input = sys.stdin.readline

c, n = map(int, input().split())
cost_info = [list(map(int, input().split())) for _ in range(n)]
cost_info.sort()

dp = [sys.maxsize for _ in range(c+100)]
dp[0] = 0

for cost, people in cost_info:
    for i in range(people, len(dp)):
        dp[i] = min(dp[i - people] + cost, dp[i])

print(min(dp[c:]))
        
