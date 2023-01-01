def solution(priorities, location):
    answer = 0
    maxnum = max(priorities)

    while True:
        checknum = priorities.pop(0)
        if maxnum == checknum:
            answer += 1
            if location != 0:
                location -= 1
            else:
                break
            maxnum = max(priorities)
        else:
            priorities.append(checknum)
            if location != 0:
                location -= 1
            else:
                location = len(priorities) - 1

    return answer
