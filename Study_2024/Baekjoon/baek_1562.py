# dp[length][digit][bitmask]

import sys
input = sys.stdin.readline
MOD = 1000000000

n = int(input())

dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(n+1)]

for i in range(1, 10):
    dp[1][i][1 << i] = 1

for length in range(2, n + 1):
    for digit in range(10):
        for bitmask in range(1 << 10):
            if digit > 0:
                dp[length][digit][bitmask | (1 << digit)] += dp[length - 1][digit - 1][bitmask]
                dp[length][digit][bitmask | (1 << digit)] %= MOD
            if digit < 9:
                dp[length][digit][bitmask | (1 << digit)] += dp[length - 1][digit + 1][bitmask]
                dp[length][digit][bitmask | (1 << digit)] %= MOD
            
result = 0
for digit in range(10):
    result += dp[n][digit][(1 << 10) - 1]
    result %= MOD
    
print(result)