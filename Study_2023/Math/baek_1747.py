import sys
input = sys.stdin.readline

def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def is_palindrome(s):
    if str(s) == str(s)[::-1]:
        return True
    return False

N = int(input())

while True:
    if is_palindrome(N) and is_prime_number(N):
        print(N)
        break
    N += 1

