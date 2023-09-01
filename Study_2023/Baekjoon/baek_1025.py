import sys
from math import sqrt

input = sys.stdin.readline
N, M = map(int, input().split())
board = [input().rstrip() for _ in range(N)]

result = -1
for i in range(N):
    for j in range(M):
        for k in range(-N, N):
            for l in range(-M, M):
                if k == 0 and l == 0:
                    continue
                num = ''
                n1 = i
                n2 = j
                while 0 <= n1 < N and 0 <= n2 < M:
                    num = num + board[n1][n2]
                    if int(sqrt(int(num))) ** 2 == int(num):
                        result = max(int(num), result)
                    n1 += k
                    n2 += l

print(result)
