import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 음수 양수 따로 처리
positive = []
negative = []

for i in arr:
    if i > 0:
        positive.append(i)
    else:
        negative.append(abs(i))

# 내림차순 정렬
positive.sort(reverse=True)
negative.sort(reverse=True)

# 음수 양수 따로 담아주기
result = []
for i in range(0, len(positive), m):
    result.append(positive[i])

for i in range(0, len(negative), m):
    result.append(negative[i])

# 왕복 거리 계산, 마지막 돌아가는 거리 빼기
result.sort()
result = 2 * sum(result) - result[-1]

print(result)