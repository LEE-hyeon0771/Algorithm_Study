N, M = map(int, input().split())

tree_height = list(map(int, input().split()))

first = 0
last = max(tree_height)
while first <= last:
    mid = (first + last) // 2

    get_height = 0      # 벌목 나무 가져가는 높이
    for i in tree_height:
        if i >= mid:
            get_height += i - mid

    if get_height >= M:     # 벌목 나무 가져가는 높이가 적어도 M보다는 큼.
        first = mid + 1
    else:
        last = mid - 1

print(last)

