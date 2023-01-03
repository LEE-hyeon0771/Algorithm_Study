from collections import deque


def solution(prices):
    answer = []
    dq = deque(prices)

    while dq:
        p = dq.popleft()
        time = 0

        for i in dq:
            time += 1
            if p > i:
                break
        answer.append(time)

    return answer