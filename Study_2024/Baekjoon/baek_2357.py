import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

tree = [0] * (4 * n)

def build(node, start, end):
    if start == end:
        tree[node] = (arr[start], arr[start])
    else:
        mid = (start + end) // 2
        build(node * 2, start, mid)
        build(node * 2 + 1, mid + 1, end)
        tree[node] = (min(tree[node * 2][0], tree[node * 2 + 1][0]), max(tree[node * 2][1], tree[node * 2 + 1][1]))
    return tree[node]

def query(node, start, end, a, b):
    if end < a or b < start:
        return (1000000000, 0)
    if a <= start and end <= b:
        return tree[node]
    mid = (start + end) // 2
    left = query(node * 2, start, mid, a, b)
    right = query(node * 2 + 1, mid + 1, end, a, b)
    return (min(left[0], right[0]), max(left[1], right[1]))

build(1, 0, n-1)
results = []
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    result = query(1, 0, n - 1, a, b)
    results.append(f"{result[0]} {result[1]}")

print("\n".join(results))
        