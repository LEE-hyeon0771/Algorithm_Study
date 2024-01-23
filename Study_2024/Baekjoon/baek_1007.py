import sys
input = sys.stdin.readline
from itertools import combinations

def min_vector_sum_length(points):
    
    comb = combinations(points, len(points) // 2)
    result = sys.maxsize
    for i in comb:
        x1 = y1 = 0
        for x, y in i:
            x1 += x
            y1 += y

        x2 = sum(x for x, _ in points) - x1
        y2 = sum(y for _, y in points) - y1
        
        vector_length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        result = min(result, vector_length)

    return result

def process_input():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        arr = []
        for _ in range(n):
            a, b = map(int, input().split())
            arr.append((a, b))

        result = min_vector_sum_length(arr)
        results.append(result)

    return results

def print_results(results):
    for result in results:
        print(result)

results = process_input()
print_results(results)