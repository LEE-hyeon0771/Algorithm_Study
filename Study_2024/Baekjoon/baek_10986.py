import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

remain = [0] * m
prefix = 0
for i in range(n):
    prefix += arr[i]
    remain[prefix % m] += 1

ans = remain[0]
for i in range(m):
    ans += remain[i] * (remain[i]-1) // 2
print(ans)
