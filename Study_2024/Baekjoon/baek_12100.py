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

'''
import sys, copy
N = int(input())
pan = []
ans = 0

for _ in range(N):
    pan.append([int(x) for x in sys.stdin.readline().rstrip().split()])

def left(board):
    for i in range(N):
        cursor = 0
        for j in range(1, N):
            if board[i][j] != 0: # 0이 아닌 값이
                tmp = board[i][j]
                board[i][j] = 0 # 일단 비워질꺼니까 0으로 바꿈

                if board[i][cursor] == 0: # 비어있으면
                    board[i][cursor] = tmp # 옮긴다

                elif board[i][cursor] == tmp: # 같으면
                    board[i][cursor] *= 2 # 합친다
                    cursor += 1
                else: # 비어있지도 않고 다른 값일때
                    cursor += 1 # pass
                    board[i][cursor] = tmp # 바로 옆에 붙임

    return board

def right(board):
    for i in range(N):
        cursor = N - 1
        for j in range(N - 1, -1, -1):

            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[i][cursor] == 0:
                    board[i][cursor] = tmp

                elif board[i][cursor] == tmp:
                    board[i][cursor] *= 2
                    cursor -= 1
                else:
                    cursor -= 1
                    board[i][cursor] = tmp
    return board

def up(board):
    for j in range(N):
        cursor = 0
        for i in range(N):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[cursor][j] == 0:
                    board[cursor][j] = tmp

                elif board[cursor][j] == tmp:
                    board[cursor][j] *= 2
                    cursor += 1

                else:
                    cursor += 1
                    board[cursor][j] = tmp
    return board

def down(board):
    for j in range(N):
        cursor = N - 1
        for i in range(N - 1, -1, -1):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[cursor][j] == 0:
                    board[cursor][j] = tmp

                elif board[cursor][j] == tmp:
                    board[cursor][j] *= 2
                    cursor -= 1

                else:
                    cursor -= 1
                    board[cursor][j] = tmp
    return board

def dfs(n, arr):
    global ans
    if n == 5:
        for i in range(N):
            for j in range(N):
                if arr[i][j] > ans:
                    ans = arr[i][j]
        return

    for i in range(4):
        copy_arr = copy.deepcopy(arr)
        if i == 0:
            dfs(n + 1, left(copy_arr))
        elif i == 1:
            dfs(n + 1, right(copy_arr))
        elif i == 2:
            dfs(n + 1, up(copy_arr))
        else:
            dfs(n + 1, down(copy_arr))

dfs(0, pan)
print(ans)       
        
'''