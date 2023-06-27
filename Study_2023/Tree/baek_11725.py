from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
visited = [0]*(N+1)
result = [0]*(N+1)

node = list([] for _ in range(N+1))
for i in range(N-1):
    while True:
        try:
            parents, child = map(int, input().split())
            break
        except ValueError:
            print("Please enter two values separated by a space.")
    node[parents].append(child)
    node[child].append(parents)

def DFS(node, v, visited):
    visited[v] = True
    stack=deque([v])
    while stack:
        w = stack.pop()
        for i in node[w]:
            if not visited[i]:
                stack.append(i)
                visited[i] = True
                result[i] = w

DFS(node, 1, visited)
for i in range(2, N+1):
    print(result[i])