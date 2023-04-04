n = int(input())

first = 0
last = n

while first <= last:
    mid = (first + last) // 2
    if pow(mid, 2) >= n:
        last = mid - 1
    else:
        first = mid + 1

print(first)