import sys
input = sys.stdin.readline

n = int(input())
wine = [int(input()) for _ in range(n)]

def max_wine(n, wine):
    dp = [0] * (n+1)
    dp[1] = wine[0]
    if n > 1:
        dp[2] = wine[0] + wine[1]
    
    for i in range(3, n+1):
        dp[i] = max(dp[i-1], dp[i-2] + wine[i-1], dp[i-3] + wine[i-2] + wine[i-1])
    
    return dp[n]

print(max_wine(n, wine))