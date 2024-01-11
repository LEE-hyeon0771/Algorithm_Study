import sys
input = sys.stdin.readline
import math

n = int(input())

# 소수 찾기
arr = [True] * (n+1)
arr[0] = False
arr[1] = False
for i in range(2, int(math.sqrt(n) + 1)):
    if arr[i]:
        for j in range(i * i, n + 1, i):
            arr[j] = False


primes = [i for i in range(2, n + 1) if arr[i]]

prefix_sum = [0] * (len(primes) + 1)
for i in range(1, len(primes) + 1):
    prefix_sum[i] = prefix_sum[i - 1] + primes[i - 1]

answer = 0
first = 0
end = 1

while first < len(primes) and primes[first] <= n:
    current_sum = prefix_sum[end] - prefix_sum[first]
    if current_sum == n:
        answer += 1
        first += 1
    elif current_sum < n and end < len(primes):
        end += 1
    else:
        first += 1

print(answer)
