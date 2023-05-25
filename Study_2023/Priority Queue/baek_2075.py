import heapq as hp
N = int(input())

Heap = []
for i in range(N):
    num_list = list(map(int, input().split()))
    for num in num_list:
        if len(Heap) < N:
            hp.heappush(Heap, num)
        else:
            if Heap[0] < num:
                hp.heappop(Heap)
                hp.heappush(Heap, num)

print(Heap[0])


