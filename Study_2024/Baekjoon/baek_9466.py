import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
t = int(input())

def dfs(i, result):
    visited[i] = 1
    team.append(i)
    if visited[arr[i]]:
        if arr[i] in team:
            result += team[team.index(arr[i]):]
        return
    else:
        dfs(arr[i], result)
            
for i in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [0 for _ in range(n+1)]
    result = []
    for i in range(1, n+1):
        if not visited[i]:
            team = []
            dfs(i, result)
    
    print(n - len(result))