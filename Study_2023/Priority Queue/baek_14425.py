N, M = map(int, input().split())

S = set([input() for i in range(N)])

count = 0
for i in range(M):
    str = input()
    if str in S:
        count += 1

print(count)