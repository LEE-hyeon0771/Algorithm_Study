import sys
input = sys.stdin.readline
maxtemp = sys.maxsize

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

for i in range(n-2):
    start = i+1
    end = n-1
    while start < end:
        temp = arr[i] + arr[start] + arr[end]
        if abs(temp) < maxtemp:
            maxtemp = abs(temp)
            result = [arr[i], arr[start], arr[end]]
        if temp < 0:
            start += 1
        elif temp > 0:
            end -= 1
        else:
            break

print(*result)