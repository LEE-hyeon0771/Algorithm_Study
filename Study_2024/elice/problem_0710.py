'''
엘리스 토끼는 문자열을 직접 압축 해제하려고 합니다.

압축되지 않은 문자열 S가 주어졌을 때, 이 문자열 중 어떤 부분 문자열은 K(Q)와 같이 압축할 수 있습니다. 이것은 Q라는 문자열이 K 번 반복된다는 뜻입니다. K는 한 자릿수의 정수이고, Q는 0자리 이상의 문자열입니다.

예를 들면, 53(8)은 다음과 같이 압축을 해제할 수 있습니다.

53(8) = 5 + 3(8) = 5 + 888 = 5888

압축된 문자열이 주어졌을 때, 이 문자열을 다시 압축을 푸는 프로그램을 작성하세요.


지시사항
입력
첫째 줄에 압축된 문자열 S를 입력합니다.
S의 길이는 최대 50입니다.
문자열은 (, ), 숫자로만 구성되어 있습니다.
출력
압축되지 않은 문자열의 길이를 출력합니다.
입력 예시
11(18(72(7)))

출력 예시
26
'''

'''
11777777777777777777777777 -> 총 26자리

숫자 만나면 숫자 끝까지 숫자를 읽음
'('는 그냥 담음
')' 만나면 temp에다가 숫자 pop 시키면서 길이 계산
stack에서 '('를 만나면 pop 시키고, repeat_count 변수에 '(' 앞의 숫자를 pop 시켜서 담아줌
temp에 담긴 숫자(문자열)들을 sum 시킨 것을 곱해서 길이에 담아줌
문자는 스택에 1을 단순히 추가

'''

string = input()

stack = []
depth_result = [0] * 50
depth = 0

for ch in string:
    if ch != ")":
        if ch == "(":
            depth += 1
            depth_result[depth] = 0
        stack += [ch]
    else:
        for i in range(len(stack) - 1, -1, -1):
            if stack[i] == "(":
                num = depth_result[depth]
                for j in stack[i + 1 :]:
                    num += 1
                depth -= 1
                depth_result[depth] += num * int(stack[i - 1])
                del stack[i - 1 :]

                break
print(depth_result[0] + len(stack))














