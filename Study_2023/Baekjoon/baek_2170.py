import sys

input = sys.stdin.readline

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort()

start = arr[0][0]
end = arr[0][1]

result = 0
for i in range(1, n):
    newStart, newEnd = arr[i]
    if newStart > end:
        result += (end - start)
        start, end = newStart, newEnd
    else:
        end = max(end, newEnd)

result += (end - start)
print(result)