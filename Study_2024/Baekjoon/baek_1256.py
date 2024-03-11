import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

def dictionary(n, m, k):
    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = 1
    for i in range(m+1):
        dp[0][i] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    def construct_string(n, m, k):
        if n == 0:
            return 'z' * m
        if m == 0:
            return 'a' * n
        if k <= dp[n-1][m]:
            return 'a' + construct_string(n-1, m, k)
        else:
            return 'z' + construct_string(n, m-1, k - dp[n-1][m])

    if k > dp[n][m]:
        return -1
    else:
        return construct_string(n, m, k)
    
print(dictionary(n, m, k))