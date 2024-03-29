import sys
import math
input = sys.stdin.readline


def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def goldbach(num):
    for i in range(2, num):
        if isPrime(i) and isPrime(num - i):
            return (i, num - i)
    return (-1, -1)

n = int(input())
if n < 8:
    print(-1)
else:
    if n % 2 == 0:
        p1, p2 = goldbach(n - 4)
        print(f"2 2 {p1} {p2}")
    else:
        p1, p2 = goldbach(n - 5)
        print(f"2 3 {p1} {p2}")