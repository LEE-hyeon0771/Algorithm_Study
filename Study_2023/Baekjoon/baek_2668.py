import sys

input = sys.stdin.readline

def dfs(num):
    if visited[num] == 0:
        visited[num] = 1
        for i in num_list[num]:
            up.add(num)
            down.add(i)
            if up == down:
                result.extend(down)
                return
            dfs(i)
    visited[num] = 0

n = int(input())
num_list = [[] for _ in range(n+1)]
for i in range(1, n+1):
    num_list[i].append(int(input()))

result = []
for i in range(1, n + 1):
    visited = [0 for _ in range(n+1)]
    up = set()
    down = set()
    dfs(i)

result = sorted(list(set(result)))
print(len(result))
for i in result:
    print(i)

