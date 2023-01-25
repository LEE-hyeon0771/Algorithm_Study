def solution(clothes):
    answer = 1
    hash_map = {}

    for i in clothes:
        if i[1] in hash_map.keys():  # 딕셔너리 안에 의상 종류가 있으면
            hash_map[i[1]].append(i[0])  # 딕셔너리에 key 갯수 추가
        else:
            hash_map[i[1]] = [i[0]]  # 딕셔너리에 key가 새롭게 입력

    for j in hash_map.values():  # j가 딕셔너리의 value
        answer *= len(j) + 1  # 안쓴 경우 고려 : + 1

    return answer - 1