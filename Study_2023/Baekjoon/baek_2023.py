import sys
from math import sqrt

input = sys.stdin.readline

n = int(input())

def isPrime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if int(num) % i == 0:
            return False
    return True

def dfs(num):
    if len(str(num)) == n:
        print(num)
    else:
        for i in range(1, 10):
            temp = num * 10 + i
            if isPrime(temp):
                dfs(temp)

dfs(2)
dfs(3)
dfs(5)
dfs(7)