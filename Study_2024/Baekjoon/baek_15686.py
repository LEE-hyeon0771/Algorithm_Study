import sys
from itertools import combinations
input = sys.stdin.readline

def calculate_chicken_distance(houses, chickens):
    total_distance = 0
    for hx, hy in houses:
        min_distance = float('inf')
        for cx, cy in chickens:
            min_distance = min(min_distance, abs(hx - cx) + abs(hy - cy))
        total_distance += min_distance
    return total_distance

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

houses = []
chicken_stores = []

for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            houses.append((r, c))
        elif city[r][c] == 2:
            chicken_stores.append((r, c))

min_chicken_distance = float('inf')

for chicken_comb in combinations(chicken_stores, M):
    min_chicken_distance = min(min_chicken_distance, calculate_chicken_distance(houses, chicken_comb))
    
print(min_chicken_distance)