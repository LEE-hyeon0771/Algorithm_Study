import sys
input = sys.stdin.readline

'''
dp[2] = 3
dp[4] = dp[2] * dp[2] + 2
dp[6] = dp[4] * dp[2] + dp[2] * 2 + 2 = 41'''
n = int(input())
dp = [0]*(31)
dp[2] = 3
dp_sum = 0

for i in range(3, n+1):
    if i % 2 == 0:
        dp[i] = dp[i-2] * dp[2] + dp_sum * 2 + 2
        dp_sum += dp[i-2]
    else:
        dp[i] = 0

print(dp[n])