# 수업종료 시간이 다음 수업 시작 시간보다 뒤 -> 새 강의실 배정
# 수업종료 시간이 다음 수업 시작 시간보다 앞 -> 기존 강의실 유지
import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()

end_time = []
heapq.heappush(end_time, arr[0][1])
for i in range(1, n):
    if arr[i][0] >= end_time[0]:
        heapq.heappop(end_time)
    heapq.heappush(end_time, arr[i][1])

print(len(end_time))