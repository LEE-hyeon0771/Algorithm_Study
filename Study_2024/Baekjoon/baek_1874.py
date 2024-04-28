import sys
input = sys.stdin.readline

n = int(input())
stack = []
flag = True
result = []

count = 1
for i in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        result.append('+')
        count += 1
    
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        flag = False

if not flag:
    print("NO")
else:
    for i in result:
        print(i)