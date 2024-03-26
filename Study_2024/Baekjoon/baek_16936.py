import sys
input = sys.stdin.readline

n = int(input())
B = list(map(int, input().split()))

def dfs(x):
    if x % 3 == 0:
        if number(x // 3):
            return dfs(x // 3)
        if number(x * 2):
            return dfs(x * 2)
    else:
        if number(x * 2):
            return dfs(x * 2)

def number(x):
    if min(B) <= x <= max(B) and (x in B) and (x not in A):
        A.append(x)
        return True
    return False

for i in B:
    A = [i]
    dfs(i)
    if len(B) == len(A):
        print(*A)
        break
        