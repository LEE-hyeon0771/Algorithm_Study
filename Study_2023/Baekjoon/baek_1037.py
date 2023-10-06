import sys

input = sys.stdin.readline

num = int(input())
answer = list(map(int, input().split()))
print(max(answer) * min(answer))