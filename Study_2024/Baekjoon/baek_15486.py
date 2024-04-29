# dp[i] = i일에 얻을 수 있는 최대 수익
# T : 상담을 완료하는데 걸리는 기간
# P : 상담을 했을 때 받을 수 있는 금액
'''
1. 상담이 퇴사 전에 끝날 경우 : 상담 끝나는 날짜로 수익 갱신
2. 상담이 퇴사 전에 끝나지 않을 경우 : 해당 날짜까지의 최대 수익 계산 - 이전 날자까지 최대 수익과 같거나 더 커짐
'''
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def max_profit(n, arr):
    dp = [0] * (n+1)
    
    for i in range(1, n+1):
        T, P = arr[i - 1]
        
        # 상담이 퇴사 전에 끝날 경우
        if i + T - 1 <= n:
            # 상담 끝나는 날짜로 수익 갱신
            dp[i + T - 1] = max(dp[i + T - 1], dp[i-1] + P)
        
        # 해당 날짜까지의 최대 수익
        dp[i] = max(dp[i], dp[i-1])
    
    return dp[n]

print(max_profit(n, arr))