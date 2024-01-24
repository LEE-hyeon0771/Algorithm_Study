# 가격을 최대힙으로 담는 것이 핵심
# 무게는 작은것부터 정렬해서 담아줘야함
# 무게와 가격을 Greedy Algorithm으로 생각하기

import sys
input = sys.stdin.readline
import heapq

n, k = map(int, input().split())
info = [list((map(int, input().split()))) for _ in range(n)]
max_bag = [int(input()) for _ in range(k)]
info.sort()
max_bag.sort()

result = 0
heap = []
for i in max_bag:
    while info and i >= info[0][0]:
        heapq.heappush(heap, -info[0][1])        # 가격을 최대힙으로 -로 담아 넣음
        heapq.heappop(info)
    if heap:
        result += heapq.heappop(heap)

print(-result)
        

