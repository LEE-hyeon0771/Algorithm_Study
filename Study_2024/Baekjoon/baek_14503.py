import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def clean_room(matrix, r, c, d):
    N = len(matrix)
    M = len(matrix[0])
    
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = [[False] * M for _ in range(N)]
    
    # 현 위치 청소
    visited[r][c] = True
    count = 1
    
    while True:
        
        # 왼쪽 방향 탐색
        cleaned = False
        for _ in range(4):
            d = (d+3) % 4
            nr = r + directions[d][0]
            nc = c + directions[d][1]
            
            # 청소하지 않은 경우 - 전진, 벽인 칸은 청소 대상에서 제외
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and matrix[nr][nc] == 0:
                visited[nr][nc] = True
                count += 1
                r, c = nr, nc
                cleaned = True
                break
        
        # 청소할 수 있는 칸 없으면 - 후진
        # 후진할 곳 없으면 break
        if not cleaned:
            nr = r - directions[d][0]
            nc = c - directions[d][1]
            if not(0 <= nr < N and 0 <= nc < M and matrix[nr][nc] == 0):
                break
            r, c = nr, nc
        
    return count

print(clean_room(arr, r, c, d))