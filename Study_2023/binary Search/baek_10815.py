def binarySearch(card, target, low, high):

    while low <= high:
        mid = (low + high) // 2
        if card[mid] == target:
            return mid
        if card[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None

N = int(input())
card = list(map(int, input().split()))

card.sort()

M = int(input())
sang = list(map(int, input().split()))

for target in sang:
    if binarySearch(card, target, 0, N-1) != None:
        print("1", end=' ')
    else:
        print("0", end=' ')

