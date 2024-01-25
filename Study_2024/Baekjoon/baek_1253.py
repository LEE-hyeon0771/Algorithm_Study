# 포인터 두 파트로 나누기 i 기준
# 두 값 더한 total이 arr의 숫자와 같으면 break 아니면 위치조정

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
count = 0

for i in range(n):
    pointer = arr[:i] + arr[i+1:]
    start = 0
    end = len(pointer) - 1
    while start < end:
        total = pointer[start] + pointer[end]
        if total == arr[i]:
            count += 1
            break
        if total < arr[i]:
            start += 1
        else:
            end -= 1

print(count)