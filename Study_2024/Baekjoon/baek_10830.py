# B 짝수 -> A^(B/2) * A^(B/2)
# B 홀수 -> A*(A^(B-1))

import sys
input = sys.stdin.readline

def mat_mul(A, B, mod):
    size = len(A)
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += A[i][k] * B[k][j]
                result [i][j] %= mod
    return result

def mat_pow(A, B, mod):
    size = len(A)
    if B == 1:
        return A
    elif B % 2 == 0:
        temp = mat_pow(A, B//2, mod)
        return mat_mul(temp, temp, mod)
    else:
        return mat_mul(A, mat_pow(A, B-1, mod), mod)
    
N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        A[i][j] %= 1000
result = mat_pow(A, B, 1000)

for row in result:
    print(' '.join(map(str, row)))
