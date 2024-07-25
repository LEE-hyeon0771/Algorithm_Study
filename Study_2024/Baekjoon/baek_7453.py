import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
A = []
B = []
C = []
D = []

for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
    
sum_dict = defaultdict(int)
for a in A:
    for b in B:
        sum_dict[a + b] += 1
    
count = 0
for c in C:
    for d in D:
        target = -(c + d)
        if target in sum_dict:
            count += sum_dict[target]

print(count)