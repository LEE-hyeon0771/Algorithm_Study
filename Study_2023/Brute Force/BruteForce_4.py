def solution(brown, yellow):
    for b in range(1, (brown + yellow) + 1):
        if ((brown + yellow) % b) == 0:
            a = (brown + yellow) / b  # a : 가로 길이, b : 세로 길이
            if (a - 2) * (b - 2) == yellow:
                return [a, b]
