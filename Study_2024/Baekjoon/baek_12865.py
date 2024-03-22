# w보다 현재 무게 낮으면 현재가치 그대로
# w보다 현재 무게 커지면 현재에서 무게를 빼고 가치를 갱신해준 값
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N+1):
    for j in range(1, K + 1):
        w, v = items[i-1]
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

print(dp[N][K])
