from itertools import permutations


def solution(k, dungeons):
    answer = 0

    for per in permutations(dungeons, len(dungeons)):
        tmp = k
        count = 0

        for min_tired, spend_tired in per:
            if tmp >= min_tired:
                tmp -= spend_tired
                count += 1

        if count > answer:
            answer = count

    return answer