import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
area_sum = arr[0]
i = 0
j = 0
result = 100001

while True:
    if area_sum >= s:
        area_sum -= arr[i]
        result = min(result, abs(i-j)+1)
        i += 1
    else:
        j += 1
        if j == n:
            break
        area_sum += arr[j]

if result == 100001:
    print(0)
else:
    print(result)