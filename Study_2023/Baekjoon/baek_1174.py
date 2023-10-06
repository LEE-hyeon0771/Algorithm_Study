import sys
from itertools import combinations

input = sys.stdin.readline
N = int(input())
result = []

for i in range(1, 11):
    for comb in combinations(range(0, 10), i):
        result.append(int(''.join(list(map(str, reversed(list(comb)))))))

result.sort()

try:
    print(result[N-1])
except:
    print(-1)