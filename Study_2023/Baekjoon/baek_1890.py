import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            print(dp[i][j])
            break

        pos = arr[i][j]
        if i + pos < n:
            dp[i + pos][j] += dp[i][j]
        if j + pos < n:
            dp[i][j + pos] += dp[i][j]