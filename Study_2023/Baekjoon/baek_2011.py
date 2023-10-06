import sys

input = sys.stdin.readline

arr = list(map(int, input().rstrip()))
length = len(arr)
dp = [0] * (length + 1)
dp[0] = 1
dp[1] = 1
if arr[0] == 0:
    print("0")
else:
    for i in range(2, length + 1):
        temp = arr[i - 2] * 10 + arr[i - 1]
        if arr[i - 1] > 0:
            dp[i] += dp[i - 1]
        if temp >= 10 and temp <= 26:
            dp[i] += dp[i - 2]
    print(dp[length] % 1000000)