from itertools import product
def solution(word):
    answer = 0

    result = [''.join(j) for i in range(0, 5) for j in product('AEIOU', repeat=i + 1)]
    result.sort()
    answer = result.index(word) + 1
    return answer