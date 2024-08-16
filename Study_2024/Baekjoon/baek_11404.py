import sys
input = sys.stdin.readline
INF = sys.maxsize

def floyd(n, edges):
    dp = [[INF] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = 0
    
    for a, b, c in edges:
        dp[a-1][b-1] = min(dp[a-1][b-1], c)
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    
    for i in range(n):
        for j in range(n):
            if dp[i][j] == INF:
                print(0, end=' ')
            else:
                print(dp[i][j], end=' ')
        
        print()

n = int(input())
m = int(input())
edges = [map(int, input().split()) for _ in range(m)]

floyd(n, edges)