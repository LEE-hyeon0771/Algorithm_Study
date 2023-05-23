import sys
import heapq as hq

input = sys.stdin.readline
N = int(input())

Heap = []

for i in range(N):
    x = int(input())
    if x == 0:
        if len(Heap) >= 1:
            print(-hq.heappop(Heap))
        else:
            print(0)

    else:
        hq.heappush(Heap, -x)


