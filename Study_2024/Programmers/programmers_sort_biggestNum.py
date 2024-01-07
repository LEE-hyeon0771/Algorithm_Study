# 가장 큰 수

def solution(numbers):
    def sorting(n):
        return str(n) * 3
    # 3을 곱하는 이유 : 1000이하의 수 이므로, 문자열을 3개씩 이어붙여서 비교하게 되면, 30 < 3으로 선택이 가능.
    numbers = list(map(str, numbers))
    numbers.sort(key=sorting, reverse=True)
    answer = ''.join(numbers)
    # 00을 0으로 처리하기 위해 str(int) 강제형 변환 두번
    return str(int(answer))