def solution(citations):
    answer = 0
    count = 0
    citations.sort()

    for i, j in enumerate(citations):
        # (0, 0)
        # (1, 1)
        # (2, 3)
        # (3, 5)
        # (4, 6)

        if j >= len(citations) - i:
            # i=0 0 >= 5-0=5 (x)
            # i=1 1 >= 5-1=4 (x)
            # i=2 3 >= 5-2=3
            # i=3 5 >= 5-3=2
            # i=4 6 >= 5-4=1
            count += 1
            answer = count

    return answer