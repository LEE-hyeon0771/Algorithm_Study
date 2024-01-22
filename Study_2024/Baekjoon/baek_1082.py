# dynamic programming + Greedy Algorithm
# 현재가격 - p + 현재 방번호
# max값을 찾으면 되므로 방 뒷번호부터 탐색


import sys
input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
arr = list(map(int, input().split()))
m = int(input())

dp = [-INF for _ in range(m+1)]

for i in reversed(range(n)):
    p_i = arr[i]
    for j in range(p_i, m+1):
        # dp[j-p_i] -> 현재가격 j - p를 통해 최대가격 탐색
        dp[j] = max(dp[j], i, dp[j-p_i]*10 + i)

print(dp[m])