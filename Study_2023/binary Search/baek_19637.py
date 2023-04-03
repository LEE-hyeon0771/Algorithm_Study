import bisect
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

name_num = []
char_num = []

for i in range(n):
    name, char = map(str, input().split())
    name_num.append(name)
    char_num.append(int(char))

for i in range(m):
    bs = int(input())
    answer = bisect.bisect_left(char_num, bs)
    print(name_num[answer])

