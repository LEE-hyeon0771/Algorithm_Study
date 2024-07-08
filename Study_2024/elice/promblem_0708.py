'''
엘리스 토끼는 목표량을 정해 수학 문제를 열심히 풉니다. 목표량은 정수입니다.

내일 풀 수학 문제의 개수는 오늘 푼 문제 개수의 수와 숫자의 구성이 같으면서, 오늘 푼 문제 개수의 수보다 큰 수 중 가장 작은 수입니다.

예를 들어, 오늘 67문제를 풀었으면 다음 날 76문제를 풉니다.

오늘 푼 문제의 개수를 줬을 때 다음날 풀 문제의 개수를 출력하는 프로그램을 작성하세요.


지시사항
입력
첫 번째 줄에 오늘 푼 문제의 개수인 자연수 N을 입력합니다.


1≤N≤999999


정답이 반드시 있는 경우만 입력값으로 주어집니다.
출력
다음날 풀 문제의 개수를 출력합니다.
입력 예시
364

출력 예시
436
'''

'''
<풀이 방법>

오른쪽 -> 왼쪽 순회하면서 숫자가 바로 다음 숫자보다 작은 첫번째 위치 탐색
찾은 위치부터 다시 이 숫자보다 큰 숫자 탐색
두 숫자 교환
교환 위치 이후 숫자 오름차순 정렬
'''

import sys
input = sys.stdin.readline

def next_number(n):
    digits = list(str(n))
    length = len(digits)

    i = length - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    
    if i == -1:
        digits.reverse()
    else:
        j = length - 1
        while digits[j] <= digits[i]:
            j -= 1

        digits[i], digits[j] = digits[j], digits[i]
        
        digits = digits[:i + 1] + sorted(digits[i + 1:])

    return int("".join(digits))

n = int(input())
print(next_number(n))