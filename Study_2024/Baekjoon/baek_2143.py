import sys
input = sys.stdin.readline
from collections import defaultdict

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

Adict = defaultdict(int)
result = 0
for i in range(n):
    for j in range(i, n):
        Adict[sum(A[i:j+1])] += 1       # A 배열의 모든 부배열의 합 갯수

for i in range(m):
    for j in range(i, m):
        result += Adict[T - sum(B[i:j+1])]      # A + B = T -> A = T - B

print(result)