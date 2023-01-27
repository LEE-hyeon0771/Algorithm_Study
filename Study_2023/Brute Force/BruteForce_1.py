def solution(sizes):
    answer = 0

    max_list = []
    min_list = []

    for i in range(len(sizes)):
        max_list.append(max(sizes[i][0], sizes[i][1]))
        min_list.append(min(sizes[i][0], sizes[i][1]))

    max_list_num = max(max_list)
    min_list_num = max(min_list)

    answer = max_list_num * min_list_num

    return answer