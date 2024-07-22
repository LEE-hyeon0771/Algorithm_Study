import sys
input = sys.stdin.readline

def solve(R, C, bakery):
    def dfs(r, c):
        if c == C-1:
            return True
        for dr in [-1, 0, 1]:
            nr = r + dr
            nc = c + 1
            if 0 <= nr < R and bakery[nr][nc] == '.' and not visited[nr][nc]:
                visited[nr][nc] = True
                if dfs(nr, nc):
                    return True
        return False

    visited = [[False] * C for _ in range(R)]
    count = 0
    
    for row in range(R):
        if bakery[row][0] == '.' and dfs(row, 0):
            count += 1
    
    return count

R, C = map(int, input().split())
bakery = [input() for _ in range(R)]

print(solve(R, C, bakery))