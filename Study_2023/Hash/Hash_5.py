def solution(genres, plays):
    answer = []
    total = {}  # {장르 : 총 재생횟수}
    dic = {}  # {장르 : [재생횟수, 고유번호]}

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        if genre in total.keys():
            total[genre] += play
        else:
            total[genre] = play

        if genre in dic.keys():
            dic[genre].append((play, i))
        else:
            dic[genre] = [(play, i)]

    # 총 재생횟수 : 내림차순 정렬 x[1]칸에 위치
    total = sorted(total.items(), key=lambda x: x[1], reverse=True)

    for key in total:
        playlist = dic[key[0]]

        # 재생횟수 : 내림차순 정렬 x[0]칸에 위치
        playlist = sorted(playlist, key=lambda x: x[0], reverse=True)
        for i in range(len(playlist)):
            if i == 2:
                break
            answer.append(playlist[i][1])
            # 재생횟수 : 내림차순 정렬 x[i][0]칸에 위치
            # 고유번호 : 오름차순 정렬 x[i][1]칸에 위치

    return answer