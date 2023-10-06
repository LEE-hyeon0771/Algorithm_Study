import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

min_arr = []
result = 0
if n == 1:
    arr.sort()
    for i in range(0, 5):
        result += arr[i]

else:
    min_arr.append(min(arr[0], arr[5]))
    min_arr.append(min(arr[1], arr[4]))
    min_arr.append(min(arr[2], arr[3]))
    min_arr = sorted(min_arr)

    min1 = min_arr[0]
    min2 = min_arr[0] + min_arr[1]
    min3 = min_arr[0] + min_arr[1] + min_arr[2]

    case1 = (n-2)**2 + (n-2) * (n-1) * 4
    case2 = 4*(n-2) + 4*(n-1)
    case3 = 4

    result += case1 * min1
    result += case2 * min2
    result += case3 * min3

print(result)