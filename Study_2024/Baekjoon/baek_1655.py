# max_heap에 속하지 않거나 max_heap의 최댓값보다 입력 수가 작다면 : left 최대힙에 num 담기(중간 수 중 작은수)
# 나머지 : right 최소힙에 num 담기
# 왼쪽에 오른쪽보다 더 큰 수 있으면 left, right 숫자 자리 바꾸기
# left의 최대 루트값 출력

import sys
import heapq

input = sys.stdin.readline

def get_medians(nums):
    min_heap = [] # right
    max_heap = [] # left
    medians = []

    for num in nums:
        if not max_heap or num < -max_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)
        
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        if len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        
        medians.append(-max_heap[0])

    return medians

nums = []
n = int(input())
for i in range(n):
    num = int(input())
    nums.append(num)

medians = get_medians(nums)
for median in medians:
    print(median)