import sys
input = sys.stdin.readline

def operations(n):
    dp = [float('inf')] * (n+1)
    previous = [0] * (n+1)
    
    dp[1] = 0
    
    for i in range(2, n+1):
        if dp[i] > dp[i-1] + 1:
            dp[i] = dp[i-1] + 1
            previous[i] = i - 1
        
        if i % 2 == 0 and dp[i] > dp[i//2] + 1:
            dp[i] = dp[i//2] + 1
            previous[i] = i//2
        
        if i % 3 == 0 and dp[i] > dp[i//3] + 1:
            dp[i] = dp[i//3] + 1
            previous[i] = i//3

    path = []
    step = n
    while step != 0:
        path.append(step)
        step = previous[step]
    
    return dp[n], path

n = int(input())
min_ops, path = operations(n)

print(min_ops)
print(' '.join(map(str, path)))
            