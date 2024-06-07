import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort()
    max_interview = 0
    result = 1
    for j in range(1, len(arr)):
        if arr[max_interview][1] > arr[j][1]:
            max_interview = j
            result += 1
    print(result)