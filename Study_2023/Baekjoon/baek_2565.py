import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort()

dp = [0] * n
for i in range(n):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += 1

print(n-max(dp))