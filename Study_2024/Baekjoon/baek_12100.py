import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0

def left(map):
    for i in range(n):
        count = 0
        for j in range(1, n):
            if map[i][j]:
                temp_map = map[i][j]
                map[i][j] = 0
                
                if map[i][count] == 0:
                    map[i][count] = temp_map
                elif map[i][count] == temp_map:
                    map[i][count] *= 2
                    count += 1
                else:
                    count += 1
                    map[i][count] = temp_map
    return map

def right(map):
    for i in range(n):
        count = n-1
        for j in range(n-1, -1, -1):
            if map[i][j]:
                temp_map = map[i][j]
                map[i][j] = 0
                
                if map[i][count] == 0:
                    map[i][count] = temp_map
                elif map[i][count] == temp_map:
                    map[i][count] *= 2
                    count -= 1
                else:
                    count -= 1
                    map[i][count] = temp_map
    return map

def up(map):
    for j in range(n):
        count = 0
        for i in range(n):
            if map[i][j]:
                temp_map = map[i][j]
                map[i][j] = 0
                
                if map[count][j] == 0:
                    map[count][j] = temp_map
                elif map[count][j] == temp_map:
                    map[count][j] *= 2
                    count += 1
                else:
                    count += 1
                    map[count][j] = temp_map
    return map

def down(map):
    for j in range(n):
        count = n-1
        for i in range(n-1, -1, -1):
            if map[i][j]:
                temp_map = map[i][j]
                map[i][j] = 0
                
                if map[count][j] == 0:
                    map[count][j] = temp_map
                elif map[count][j] == temp_map:
                    map[count][j] *= 2
                    count -= 1
                else:
                    count -= 1
                    map[count][j] = temp_map
    return map

def dfs(arr, depth):
    global result
    if depth == 5:
        for i in range(n):
            for j in range(n):
                if arr[i][j] > result:
                    result = arr[i][j]
        return
    
    for i in range(4):
        if i == 0:
            dfs(left(deepcopy(arr)), depth+1)
        elif i == 1:
            dfs(right(deepcopy(arr)), depth+1)
        elif i == 2:
            dfs(up(deepcopy(arr)), depth+1)
        else:
            dfs(down(deepcopy(arr)), depth+1)
            
dfs(arr, 0)      
print(result)