N, M = map(int, input().split())

min_ham_d = ''
ham_count = 0
DNA = [input() for i in range(N)]


for i in range(M):               # M: 열
    DNA_idx = [0, 0, 0, 0]          # DNA_idx : DNA 빈도수
    for j in range(N):           # N: 행
        if DNA[j][i] == 'A':
            DNA_idx[0] += 1
        elif DNA[j][i] == 'C':
            DNA_idx[1] += 1
        elif DNA[j][i] == 'G':
            DNA_idx[2] += 1
        elif DNA[j][i] == 'T':
            DNA_idx[3] += 1

    max_idx = DNA_idx.index(max(DNA_idx))

    if max_idx == 0:
        min_ham_d += 'A'
    elif max_idx == 1:
        min_ham_d += 'C'
    elif max_idx == 2:
        min_ham_d += 'G'
    elif max_idx == 3:
        min_ham_d += 'T'

    ham_count += N - max(DNA_idx)

print(min_ham_d)
print(ham_count)