import sys

input = sys.stdin.readline

def dfs(arr, num):
    arr[num] = -2
    for i in range(len(arr)):
        if arr[i] == num:   # num : 삭제한 인덱스, i : 삭제한 인덱스를 부모로 가지는 arr의 인덱스 위치
            dfs(arr, i)


N = int(input())
parents_list = list(map(int, input().split()))
remove_num = int(input())

dfs(parents_list, remove_num)
count = 0
for i in range(N):
    if parents_list[i] != -2:
        if i not in parents_list:
            count += 1

print(count)
