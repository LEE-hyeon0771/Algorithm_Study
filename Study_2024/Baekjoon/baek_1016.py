import sys
input = sys.stdin.readline

min_, max_ = map(int, input().split())

def count_squarefree(min_val, max_val):
    range_size = max_val - min_val + 1
    
    sqaure_free = [True] * range_size
    
    i = 2
    while i**2 <= max_val:
        square = i**2
        start = ((min_val + square - 1) // square) * square
        
        if start < min_val:
            start += square
        
        for j in range(start, max_val + 1, square):
            sqaure_free[j - min_val] = False
            
        i += 1
    
    return sum(sqaure_free)

print(count_squarefree(min_, max_))