from itertools import combinations

N, M = map(int, input().split())

chicken_like = []

for i in range(N):
    chicken_like.append(list(map(int, input().split())))

maxsum = 0
for a,b,c in combinations(range(M), 3):
    count = 0
    for i in range(N):
        count += max(chicken_like[i][a],chicken_like[i][b],chicken_like[i][c])

    maxsum = max(maxsum, count)

print(maxsum)

