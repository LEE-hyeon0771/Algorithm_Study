def solution(progresses, speeds):
    answer = []
    count = 0

    while len(progresses) > 0:
        if progresses[0] + speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count = count + 1

        else:
            if count > 0:
                answer.append(count)
                count = 0
            for i in range(len(progresses)):
                progresses[i] = progresses[i] + speeds[i]

    answer.append(count)

    return answer