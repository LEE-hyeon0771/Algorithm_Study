import sys

input = sys.stdin.readline
answer = 2000000000
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

first = 0
end = n - 1

while first < end:
    left = arr[first]
    right = arr[end]
    total_sum = left + right

    if abs(total_sum) <= answer:
        a = arr[first]
        b = arr[end]
        answer = abs(total_sum)

    if total_sum < 0:
        first += 1
    else:
        end -= 1

print(a, b)