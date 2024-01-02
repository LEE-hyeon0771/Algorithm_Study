import sys
input = sys.stdin.readline

def is_possible(distance, locations, min_count):
    count = 1
    last_location = locations[0]

    for location in locations:
        if location - last_location >= distance:
            count += 1
            last_location = location

    return count >= min_count

def binary_search(locations, min_count):
    start = 1
    end = locations[-1] - locations[0]
    result = 0

    while start <= end:
        mid = (start + end) // 2
        if is_possible(mid, locations, min_count):
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result

n, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

answer = binary_search(arr, c)
print(answer)
