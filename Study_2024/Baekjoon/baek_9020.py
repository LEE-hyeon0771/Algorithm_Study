import sys
input = sys.stdin.readline
import math

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

arr = []
n = int(input())
for i in range(n):
    num = int(input())
    one = num // 2
    two = num // 2
    while one > 0:
        if isPrime(one) and isPrime(two):
            arr.append(f"{one} {two}")
            break
        else:
            one -= 1
            two += 1
            
for result in arr:
    print(result)