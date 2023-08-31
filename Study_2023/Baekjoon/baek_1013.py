import sys
import re

input = sys.stdin.readline

num = int(input())
for i in range(num):
    sign = input().rstrip()
    result = re.compile('(100+1+|01)+')

    if result.fullmatch(sign):
        print("YES")
    else:
        print("NO")
