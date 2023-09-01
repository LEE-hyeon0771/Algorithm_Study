import sys

input = sys.stdin.readline

num = int(input())
text1 = list(input())
for i in range(num - 1):
    text2 = list(input())
    for j in range(len(text1)):
        if text1[j] != text2[j]:
            text1[j] = '?'

print(''.join(text1))
