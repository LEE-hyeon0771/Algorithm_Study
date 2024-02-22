# sorting 된 입력 arr의 index와 순차탐색하는 n까지의 index i를 뺀 값의 최댓값

import sys
input = sys.stdin.readline

n = int(input())
arr = [(int(input()), i) for i in range(n)]
sort_arr = sorted(arr, key=lambda x : x[0])

result = []
for i in range(n):
    result.append(sort_arr[i][1] - i)
max_num = max(result) + 1
print(max_num)
