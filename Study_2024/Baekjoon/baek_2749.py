import sys
input = sys.stdin.readline

def matrix_mult(A, B, mod):
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod]]

def matrix_pow(mat, exp, mod):
    res = [[1,0], [0, 1]]
    base = mat
    
    while exp:
        if exp % 2 == 1:
            res = matrix_mult(res, base, mod)
        base = matrix_mult(base, base, mod)
        exp //= 2
    
    return res

def fib_mod_n(n, mod):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    F = [[1, 1], [1, 0]]
    
    result_matrix = matrix_pow(F, n-1, mod)
    return result_matrix[0][0]

n = int(input())
print(fib_mod_n(n, 1000000))