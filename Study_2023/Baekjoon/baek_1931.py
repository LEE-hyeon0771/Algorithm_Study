import sys

input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    start, end = map(int, input().split())
    arr.append([start, end])

arr.sort(key=lambda x : x[0])
arr.sort(key=lambda x : x[1])

final = 0
count = 0
for i, j  in arr:
    if i >= final:
        count += 1
        final = j

print(count)

