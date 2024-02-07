# 사진틀을 나타내는 리스트
# 각 요소는 (학생 번호, 추천 횟수, 게시된 순서)를 나타내는 튜플

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
recommend = list(map(int, input().split()))

frames = []  
time_stamp = 0  

for student in recommend:
    found = False
    for i in range(len(frames)):
        if frames[i][0] == student:
            frames[i] = (frames[i][0], frames[i][1] + 1, frames[i][2])
            found = True
            break
    
    if not found:
        if len(frames) < n:
            frames.append((student, 1, time_stamp))
        else:
            # 추천 횟수가 가장 적고, 가장 오래된 사진을 찾아 제거
            frames.sort(key=lambda x: (x[1], x[2]))
            frames.pop(0)
            frames.append((student, 1, time_stamp))
    time_stamp += 1  

final_candidates = sorted([student[0] for student in frames])
print(' '.join(map(str, final_candidates)))