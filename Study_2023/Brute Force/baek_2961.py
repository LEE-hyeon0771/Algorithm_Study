from itertools import combinations

N = int(input())

S_arr = []
B_arr = []
for i in range(N):
    S, B = map(int, input().split())
    S_arr.append(S)
    B_arr.append(B)

answer = 1000000000

for i in range(1, N+1):
    comb = list(combinations(list(range(N)),i))

    for foods in comb:
        S = 1
        B = 0
        for j in range(i):
            S *= S_arr[foods[j]]
            B += B_arr[foods[j]]
        answer = min(answer, abs(S-B))

print(answer)


