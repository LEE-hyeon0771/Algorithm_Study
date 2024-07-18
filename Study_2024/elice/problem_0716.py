'''
계기판 조작하기
시간 제한: 1초
엘리스는 악질 중고차 딜러인 체셔를 싫어해 체셔를 골탕 먹이려고 합니다.

엘리스는 순식간에 자동차 주행거리 계기판을 조작할 수 있는 기술을 가지고 있습니다. 엘리스는 차를 구경하겠다고 체셔에게 부탁한 뒤 구경하는 시간 동안 계기판의 주행거리를 더 크게 조작해 체셔가 당황하게 만들 예정입니다.

원래 자동차의 주행거리가 N킬로미터면 여러분은 체셔에게 들키지 않도록 주행거리를 N보다 크면서, 가장 작은 수로 늘려놓으려고 합니다. 이때, 조작한 값은 서로 다른 K개의 숫자로 이루어져야 합니다. 예를 들어, 100000이란 수는 1과 0으로 이루어져 있으므로, 2개의 숫자로 이루어진 수입니다.

N과 K를 줬을 때 조작할 수 있는 주행거리의 최솟값을 출력하는 프로그램을 작성하세요.


지시사항
입력
첫 번째 줄에 자연수 N과 K를 입력합니다.
1≤N≤10 
7
 

1≤K≤10
주행거리를 조작한 값이 전과 비교해 더 큰 경우만 입력합니다.
출력
첫 번째 줄에 조작할 수 있는 주행거리의 최솟값을 출력합니다.
입력 예시
100000 3

출력 예시
100002

'''

import sys
input = sys.stdin.readline

def find_next_number_with_k_unique_digits(N, K):
    if K == 10:
        return "1023456789"
    elif K == 9:
        return "102345678"
    else:
        cnt = 0
        while cnt != K:
            digit = [False] * 10
            cnt = 0
            N = str(int(N) + 1)
            for char in N:
                digit[int(char)] = True
            cnt = sum(digit)
        return N

data = input().split()
N = data[0]
K = int(data[1])
result = find_next_number_with_k_unique_digits(N, K)
print(result + '\n')