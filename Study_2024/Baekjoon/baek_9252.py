# 문자가 서로 같은 경우 이전 위치 [i-1][j-1] 위치에 1을 더함.
# 문자가 서로 다른 경우 이전 단계에서 max(len(lcs))를 현재 위치에 저장
# lcs를 dp배열을 역추적하면서 구해냄.
str1 = input()
str2 = input()

dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(str1)][len(str2)])

lcs = ''
i = len(str1)
j = len(str2)
while i > 0 and j > 0:
    if dp[i][j] == dp[i-1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j-1]:
        j -= 1
    else:
        lcs = str1[i-1] + lcs
        i -= 1
        j -= 1
if lcs:
    print(lcs)
