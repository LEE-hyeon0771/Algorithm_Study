import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [i for i in range(n+1)]

def find(i):       # 부모찾기
    if arr[i] != i:
        arr[i] = find(arr[i])
    return arr[i]

def union(a, b):   # 합집합
    a = find(a)
    b = find(b)

    if a < b:
        arr[b] = a
    else:
        arr[a] = b

for i in range(m):
    check, a, b = map(int, input().split())
    if check == 0:
        union(a, b)
    elif check == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")