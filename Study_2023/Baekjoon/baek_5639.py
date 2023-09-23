import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def postorder(first, end):
    if first > end:
        return
    mid = end + 1
    for i in range(first + 1, end + 1):
        if lst[first] < lst[i]:
            mid = i
            break
    postorder(first + 1, mid - 1)
    postorder(mid, end)
    print(lst[first])

lst = []
while True:
    try:
        lst.append(int(input()))
    except:
        break

postorder(0, len(lst) - 1)
