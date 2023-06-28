import sys
input = sys.stdin.readline

N = int(input())
length = list(map(int, input().split()))
node = list(map(int, input().split()))

answer = 0
min_node = node[0]

for i in range(N-1):
    if node[i] < min_node:
        min_node = node[i]
    answer += min_node * length[i]

print(answer)

