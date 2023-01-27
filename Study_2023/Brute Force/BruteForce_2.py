def solution(answers):
    answer = []

    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    count1 = 0
    count2 = 0
    count3 = 0

    for i in range(len(answers)):
        if answers[i] == first[i % len(first)]:
            count1 += 1
        if answers[i] == second[i % len(second)]:
            count2 += 1
        if answers[i] == third[i % len(third)]:
            count3 += 1

    count_list = [count1, count2, count3]

    for i in range(len(count_list)):
        if count_list[i] == max(count_list):
            answer.append(i + 1)

    answer.sort()

    return answer