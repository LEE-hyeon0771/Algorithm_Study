# 이진탐색 사용해야함.
# n은 10^5 보다 작거나 같은 자연수
# k는 min(10^9, N^2)
# x // i : i*j <= x 에서 최대 j. 행 i에서 값 x보다 작은 개수들
# n : 배열 A 크기, i*j에서 j의 최댓값, 배열이 n*n 크기이기 때문에 j의 값이 1~n
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

def count(x, n):
    count = 0
    for i in range(1, n+1):
        count += min(x // i, n)
    return count

def find_num(n, k):
    start, end = 1, k
    while start <= end:
        mid = (start + end) // 2
        if count(mid, n) >= k:
            end = mid - 1
        else:
            start = mid + 1
    return start

num = find_num(n, k)
print(num)