from itertools import permutations

N = int(input())
K = int(input())

lists = []
for i in range(N):
    lists.append((input()))

answer = set()
for i in permutations(lists, K):
    answer.add(''.join(i))

print(len(answer))