import sys

input = sys.stdin.readline

n, m = map(int, input().split())
matrix1 = [list(map(int, input().rstrip())) for _ in range(n)]
matrix2 = [list(map(int, input().rstrip())) for _ in range(n)]

def change(i, j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            matrix1[x][y] = 1 - matrix1[x][y]

count = 0
for i in range(n-2):
    for j in range(m-2):
        if matrix1[i][j] != matrix2[i][j]:
            change(i, j)
            count += 1

flag = False
for i in range(n):
    for j in range(m):
        if matrix1[i][j] != matrix2[i][j]:
            flag = True
            break

if flag:
    print(-1)
else:
    print(count)