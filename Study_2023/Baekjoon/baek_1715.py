import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    heapq.heappush(arr, int(input()))

result = 0
for i in range(n-1):
    first = heapq.heappop(arr)
    second = heapq.heappop(arr)
    temp = first + second
    result += temp
    heapq.heappush(arr, temp)
print(result)