import sys
input = sys.stdin.readline
from collections import deque

target = "123456780"
directions = [(-1,0), (1,0), (0, -1), (0,1)]

def bfs(start):
    q = deque([(start, start.index("0"), 0)])
    visited = set()
    visited.add(start)
    
    while q:
        curr, zero, depth = q.popleft()
        
        if curr == target:
            return depth
        
        x, y = divmod(zero, 3)
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            
            if 0<= nx < 3 and 0 <= ny < 3:
                new_zero = nx * 3 + ny
                new_state = list(curr)
                new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]
                new_state = ''.join(new_state)
                
                if new_state not in visited:
                    visited.add(new_state)
                    q.append((new_state, new_zero, depth + 1))
    return -1

initial = ''
for _ in range(3):
    initial += ''.join(input().split())

print(bfs(initial))