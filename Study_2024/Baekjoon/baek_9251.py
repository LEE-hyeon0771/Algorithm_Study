# 문자열 갯수가 dp보다 작으면 그대로
# 문자열 비교 시 같으면 갯수 +1
# 최대 갯수 출력
str1 = input()
str2 = input()

dp = [0] * len(str2)

for i in range(len(str1)):
    count = 0
    for j in range(len(str2)):
        if count < dp[j]:
            count = dp[j]
        elif str1[i] == str2[j]:
            dp[j] = count + 1

print(max(dp))