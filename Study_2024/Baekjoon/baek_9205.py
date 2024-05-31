import sys
input = sys.stdin.readline
from collections import deque

t = int(input().strip())

def reach_festival(house, store, festival):
    q = deque([house])
    visited = set()
    visited.add(house)
    
    while q:
        curr_location = q.popleft()
        if distance(curr_location, festival) <= 1000:
            return "happy"
        for stores in store:
            if stores not in visited and distance(curr_location, stores) <= 1000:
                visited.add(stores)
                q.append(stores)
    return "sad"

def distance(loc1, loc2):
    return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])

result = []
for _ in range(t):
    n = int(input().strip())
    house = tuple(map(int, input().strip().split()))
    store = [tuple(map(int, input().strip().split())) for _ in range(n)]
    festival = tuple(map(int, input().strip().split()))
    result.append(reach_festival(house, store, festival))

print(*result)