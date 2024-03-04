import sys
input = sys.stdin.readline
import heapq

n = int(input())
arr = []
for _ in range(n):
    deadline, cup = map(int, input().split())
    arr.append((deadline, cup))

arr.sort()
solve = []

# sol[1] : 컵라면 수, sol[0] : 데드라인
for sol in arr:
    heapq.heappush(solve, sol[1])
    if sol[0] < len(solve):
        heapq.heappop(solve)

print(sum(solve))
        
    
