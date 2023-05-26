import sys
import heapq as hp
input = sys.stdin.readline

num = int(input())
Heap = []

for i in range(num):
    x = int(input())
    if x != 0:
        hp.heappush(Heap, (abs(x), x))
    else:
        if Heap:
            print(hp.heappop(Heap)[1])
        else:
            print(0)
