import sys
input = sys.stdin.readline

directions = [(-1,0), (1,0), (0,-1), (0,1)]

def dfs(x, y, n, grid, visited):
    
    stack = [(x, y)]
    visited[x][y] = True
    count = 0
    
    while stack:
        cx, cy = stack.pop()
        count += 1
        
        for dx, dy in directions:
            nx = cx + dx
            ny = cy + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                stack.append((nx, ny))
    
    return count

def find(n, grid):
    visited = [[False] * n for _ in range(n)]
    complexes = []
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1 and not visited[i][j]:
                complex_size = dfs(i, j, n, grid, visited)
                complexes.append(complex_size)
    return sorted(complexes)

n = int(input())
grid = [list(map(int, input().rstrip())) for _ in range(n)]

complexes = find(n, grid)

print(len(complexes))
for complex_size in complexes:
    print(complex_size)
                