import math
from itertools import permutations


def solution(numbers):
    answer = 0
    count = 0
    result = []
    for i in range(len(numbers)):
        result.append(list(set(map(int, map("".join, permutations(numbers, i + 1))))))
    result = list(set(map(int, set(sum(result, [0])))))

    for i in result:
        if isPrime_num(i) == True:
            count += 1
    answer = count
    return answer


def isPrime_num(num):
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True