import sys

input = sys.stdin.readline

n, m = map(int, input().split())
t_list = list(map(int, input().split()))[1:]
party = []

for i in range(m):
    party.append(list(map(int, input().split()))[1:])

def max_party(n, m, t_list, party):

    changed = True

    while changed:
        changed = False
        for j in party:
            if set(j) & set(t_list):
                t_length = len(t_list)
                t_list = list(set(t_list).union(set(j)))
                if t_length != len(t_list):
                    changed = True

    answer = 0
    for j in party:
        if not set(j) & set(t_list):
            answer += 1

    return answer

answer = max_party(n, m, t_list, party)
print(answer)