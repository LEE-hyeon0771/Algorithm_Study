import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
operators = list(map(int, input().split()))

ops = []
symbols = ['+', '-', '*', '/']
for i, count in enumerate(operators):
    ops.extend([symbols[i]] * count)

min_value = float('inf')
max_value = float('-inf')

def backtracking(index, curr_value, plus, minus, mul, div):
    global min_value, max_value, num, n
    
    if index == n:
        max_value = max(max_value, curr_value)
        min_value = min(min_value, curr_value)
        return
    
    if plus > 0:
        backtracking(index + 1, curr_value + num[index], plus - 1, minus, mul, div)
    if minus > 0:
        backtracking(index + 1, curr_value - num[index], plus, minus - 1, mul, div)
    if mul > 0:
        backtracking(index + 1, curr_value * num[index], plus, minus, mul - 1, div)
    if div > 0:
        if curr_value < 0:
            next_value = -(-curr_value // num[index])
        else:
            next_value = curr_value // num[index]
        backtracking(index + 1, next_value, plus, minus, mul, div - 1)
        

backtracking(1, num[0], operators[0], operators[1], operators[2], operators[3])

print(max_value)
print(min_value)
    
    