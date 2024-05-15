import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [0] * (N+1)
for i in range(1, N+1):
    arr[i] = int(input())

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

tree = [0] * (4 * N)
build(1, 1, N)
outputs = []
for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, 1, N, b, c)
    elif a == 2:
        outputs.append(query(1, 1, N, b, c))

for result in outputs:
    print(result)
