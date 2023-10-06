import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

first = 0
end = n - 1
result = [arr[first], arr[end]]
answer = abs(arr[first] + arr[end])

while first < end:
    left = arr[first]
    right = arr[end]
    total_sum = left + right

    if abs(total_sum) < answer:
        answer = abs(total_sum)
        result = [left, right]

    if total_sum < 0:
        first += 1
    else:
        end -= 1

print(result[0], result[1])

