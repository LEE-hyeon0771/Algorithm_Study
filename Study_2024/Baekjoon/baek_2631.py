import sys
input = sys.stdin.readline

n = int(input())
arr = []
dp = [0]*n
for i in range(n):
    arr.append(int(input()))
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += 1
print(n-max(dp))