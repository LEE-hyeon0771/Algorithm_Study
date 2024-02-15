import sys
input = sys.stdin.readline
from collections import deque

def read_input():
    n, m = map(int, input().split())
    arr = [[] for _ in range(n+1)]
    in_Degree = [0 for _ in range(n+1)]

    for i in range(m):
        a, b = map(int, input().split())
        arr[a].append(b)
        in_Degree[b] += 1
    return n, arr, in_Degree

def sorting(n, arr, in_Degree):   
    q = deque()
    for i in range(1, n+1):
        if in_Degree[i] == 0:
            q.append(i)

    result = []
    while q:
        curr = q.popleft()
        result.append(curr)
        for i in arr[curr]:
            in_Degree[i] -= 1
            if in_Degree[i] == 0:
                q.append(i)
    return result

n, arr, in_Degree = read_input()
sorted_students = sorting(n, arr, in_Degree)
print(*sorted_students, sep=" ")