# Lis 리스트의 마지막 값이 port 리스트보다 작으면 Lis에 담아준다. -> 이 길이 출력
# 만약 더 크다면 해당 포트 위치 검색 후 업데이트


import sys
input = sys.stdin.readline

def binary_search(arr, target, start, end):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid
    return start

n = int(input())
port = list(map(int, input().split()))

Lis = [port[0]]
for i in port[1:]:
    if Lis[-1] < i:
        Lis.append(i)
    else:
        idx = binary_search(Lis, i, 0, len(Lis))
        Lis[idx] = i

print(len(Lis))