import sys
input = sys.stdin.readline

cal = input().split('-')

result = 0
for i in cal[0].split('+'):
    result += int(i)
for i in cal[1:]:
    for j in i.split('+'):
        result -= int(j)

print(result)