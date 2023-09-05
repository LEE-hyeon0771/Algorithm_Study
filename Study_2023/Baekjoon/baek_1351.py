import sys

input = sys.stdin.readline

def dfs(i):
    if i in dict:
        return dict[i]
    else:
        dict[i] = dfs(i//P) + dfs(i//Q)
        return dict[i]
N, P, Q = map(int, input().split())
dict = {}
dict[0] = 1
print(dfs(N))