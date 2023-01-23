def solution(nums):
    answer = 0

    list_num = list(set(nums))

    answer = min(len(list_num), len(nums) / 2)

    return answer