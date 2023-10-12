import sys

input = sys.stdin.readline

def DAC(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 != 0:
        return ((DAC(a, b//2, c)**2)*a)%c
    else:
        return (DAC(a, b//2, c)**2)%c

a, b, c = map(int, input().split())

result = DAC(a, b, c)

print(result)