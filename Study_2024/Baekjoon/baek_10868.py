import sys
input = sys.stdin.readline

def build_segment_tree(left, right, i):
    if left == right:
        segment_tree[i] = nums[left]
        return segment_tree[i]
    mid = (right + left) // 2
    segment_tree[i] = min(build_segment_tree(left, mid, i * 2), build_segment_tree(mid + 1, right, i * 2 + 1))
    return segment_tree[i]

def query_min(start, end, idx, left, right):
    if left > end or right < start:
        return float('inf')
    if left <= start and right >= end:
        return segment_tree[idx]
    mid = (start + end) // 2
    return min(query_min(start, mid, idx * 2, left, right), query_min(mid + 1, end, idx * 2 + 1, left, right))

def update(start, end, node, idx, val):
    if start > idx or idx > end:
        return segment_tree[node]
    if start == end:
        segment_tree[node] = val
        return segment_tree[node]
    mid = (start + end) // 2
    segment_tree[node] = min(update(start, mid, node * 2, idx, val), update(mid + 1, end, node * 2 + 1, idx, val))
    return segment_tree[node]

n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]
queries = [tuple(map(int, input().split())) for _ in range(m)]

segment_tree = [0] * (4*n)
build_segment_tree(0, n-1, 1)

results = []
for i, j in queries:
    result = query_min(0, n-1, 1, i-1, j-1)
    results.append(result)

for result in results:
    print(result)