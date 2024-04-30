import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
for i in range(n):
    func = input().rstrip()
    m = int(input())
    arr = input().rstrip()
    q = deque(arr[1:-1].split(','))
    result = []
    if m == 0:
        q = deque()
    
    count = 0
    for i in range(len(func)):
        if func[i] == 'R':
            count += 1
        elif func[i] == 'D':
            if len(q) == 0:
                print('error')
                break
            else:
                if count % 2 == 0:
                    q.popleft()
                else:
                    q.pop()
    
    
    else:
        if count % 2 == 0:
            result.append('[' + ",".join(q) + ']')
        else:
            q.reverse()
            result.append('[' + ",".join(q) + ']')
    
    for results in result:
        print(results)