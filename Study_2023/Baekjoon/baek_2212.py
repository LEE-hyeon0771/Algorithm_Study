import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
dist = list(map(int, input().split()))

dist.sort()

result = []
for i in range(n-1):
    result.append(dist[i+1] - dist[i])

result.sort()
print(sum(result[:n-k]))