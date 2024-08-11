import sys
input = sys.stdin.readline
INF = float('inf')

def simulation(N, H, ladder):
    for start in range(N):
        pos = start
        for h in range(H):
            # 왼쪽 이동 체크
            if pos > 0 and ladder[h][pos - 1]:
                pos -= 1
            # 오른쪽 이동 체크
            elif pos < N - 1 and ladder[h][pos]:
                pos += 1
        if pos != start:
            return False
    return True

def dfs(N, H, ladder, count, x, y):
    if simulation(N, H, ladder):
        return count
    if count == 3:
        return INF
    
    min_add = INF
    for i in range(x, H):
        if i == x:
            start_j = y         # 이전 단계 다음인 y부터 시작하게 하기 위해서
        else:
            start_j = 0
        for j in range(start_j, N - 1):
            # 가로선 없는 경우
            if ladder[i][j] == 0:
                # 가로선이 연속되거나 접하면 넘어가(왼, 오른쪽 탐색)
                if (j > 0 and ladder[i][j-1]) or (j < N - 2 and ladder[i][j+1]):
                    continue
                ladder[i][j] = 1   # 가로선 추가
                min_add = min(min_add, dfs(N, H, ladder, count + 1, i, j+2))
                ladder[i][j] = 0   # 백트래킹으로 그엇던 가로선 제거
                
    return min_add

N, M, H = map(int, input().split())
ladder = [[0] * (N-1) for _ in range(H)]

for i in range(M):
    a, b = map(int, input().split())
    ladder[a-1][b-1] = 1
    
answer = dfs(N, H, ladder, 0, 0, 0)

if answer > 3:
    print(-1)
else:
    print(answer)
                
