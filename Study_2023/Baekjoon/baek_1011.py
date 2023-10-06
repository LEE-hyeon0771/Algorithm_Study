import sys

input = sys.stdin.readline

num = int(input())
for i in range(num):
    x, y = map(int, input().split())

    d = y - x

    n = 0         # 이동횟수의 반복수
    count = 0     # 공간 장치 이동횟수
    temp = 0      # 이동 거리

    while temp < d:
        count += 1
        if count % 2 != 0:
            n += 1
        temp += n

    print(count)