from collections import deque

N = int(input())

list_num = deque([i for i in range(1, N+1)])

while len(list_num) > 1:
    list_num.popleft()
    list_num.append(list_num.popleft())

print(list_num[0])