from itertools import product
N, K_number = map(int, input().split())

K = list(map(int, input().split()))
K_length = len(str(N))

while(True):
    temp = list(product(K, repeat = K_length))
    answer = []
    for i in temp:
        num = int(''.join(map(str, i)))
        if num <= N:
            answer.append(num)
    if len(answer) >= 1:
        print(max(answer))
        break
    else:
        K_length -= 1
