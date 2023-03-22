from itertools import permutations

N = int(input())

number = ['1','2','3','4','5','6','7','8','9']
answer = list(permutations(number, 3))

for i in range(N):
    num, strike, ball = map(int, input().split())
    lists = list(str(num))
    count = 0
    for j in range(len(answer)):
        j = j - count     #항상 0 index부터 비교시작
        strike_count = 0
        ball_count = 0
        for k in range(3):
            if answer[j][k] == lists[k]:    #answer sheet와 입력 숫자를 index 비교해서 같으면 strike
                strike_count += 1
            elif lists[k] in answer[j]:     #입력숫자가 answer sheet와 같지는 않은데 안에 있으면 ball
                ball_count += 1
        if strike_count != strike or ball_count != ball:
            answer.remove(answer[j])
            count += 1         #strike와 ball이 수에 맞지 않으면 해당 index를 answer 배열에서 제거

print(len(answer))