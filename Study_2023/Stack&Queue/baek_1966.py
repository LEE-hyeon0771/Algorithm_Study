case = int(input())

for i in range(case):
    N, M = map(int,input().split())
    rate = list(map(int, input().split()))
    count = 0

    while M != -1:
        if rate[0] == max(rate):    # 우선순위가 가장 높은 것을 만난 경우
            rate.pop(0)
            M -= 1
            count += 1
        else:                       # 우선순위 높은게 뒤에 있는 경우
            rate.append(rate.pop(0))

            if M == 0:              # 0번째 숫자인 경우
                M = len(rate) - 1   # 맨뒤로
            else:                   # 0번째 숫자 아닌 경우
                M -= 1              # M 1칸 줄이기

    print(count)

