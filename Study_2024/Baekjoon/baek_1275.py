import sys
input = sys.stdin.readline

def build(node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        build(node * 2, start, mid)
        build(node * 2 + 1, mid + 1, end)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]
        
def update(node, start, end, idx, val):
    # idx, val : 해당 인덱스에 새로운 값 val 저장
    if start == end:
        tree[node] = val
    else:
        mid = (start + end) // 2
        if start <= idx <= mid:
            update(node * 2, start, mid, idx, val)
        else:
            update(node * 2 + 1, mid + 1, end, idx, val)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]
        
def query(node, start, end, l, r):
    # l, r : query 시작 끝 인덱스
    if r <start or end < l:
        return 0
    if l <= start and end <= r:
        return tree[node]
    mid = (start + end) // 2
    left_sum = query(node * 2, start, mid, l, r)
    right_sum = query(node * 2 + 1, mid + 1, end, l, r)
    return left_sum + right_sum

N, Q = map(int, input().split())
arr = list(map(int, input().split()))

queries = []
for _ in range(Q):
    x, y, a, b = map(int, input().split())
    queries.append((x, y, a, b))
    
tree = [0] * (4*N + 1)
build(1, 0, N-1)

results = []
for x, y, a, b in queries:
    if x > y:
        x, y = y, x
    sum_result = query(1, 0, N-1, x-1, y-1)
    results.append(sum_result)
    update(1, 0, N-1, a-1, b)

for result in results:
    print(result)