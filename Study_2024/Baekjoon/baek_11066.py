# dp : 두 파일을 합칠 때 최소 비용 저장
# sum_matrix : 파일 크기의 부분 합 저장

import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    k = int(input().strip())
    arr = list(map(int, input().strip().split()))
    
    # total : 파일 크기의 누적합
    total = [0] * (k + 1)
    for i in range(1, k + 1):
        total[i] = total[i - 1] + arr[i - 1]
    
    dp = [[0] * k for _ in range(k)]
    sum_matrix = [[0] * k for _ in range(k)]

    for i in range(k):
        sum_matrix[i][i] = arr[i]
        for j in range(i + 1, k):
            sum_matrix[i][j] = sum_matrix[i][j - 1] + arr[j]

    for length in range(2, k + 1):
        for i in range(k - length + 1):
            j = i + length - 1   # 부분 배열의 끝 인덱스
            dp[i][j] = float('inf')
            for mid in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid + 1][j] + sum_matrix[i][j])

    print(dp[0][k - 1])
    
    
    # 40 30 30 50 
    
# mid = 1 -> 40 30 / 30 50  -> 70 + 80 + 150 =  300