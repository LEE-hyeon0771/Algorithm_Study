'''
인오더 : 왼 -> 루트 -> 오
포스트오더 : 왼 -> 오 -> 루트
프리오더 : 루트 -> 왼 -> 오
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

def find_preorder(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return
    
    root = postorder[post_end]
    preorder.append(root)
    
    root_idx = inorder_idx[root]
    left_subtree_size = root_idx - in_start
    
    find_preorder(in_start, root_idx - 1, post_start, post_start + left_subtree_size - 1)
    find_preorder(root_idx + 1, in_end, post_start + left_subtree_size, post_end - 1)
    
n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

inorder_idx = {value: idx for idx, value in enumerate(inorder)}
preorder = []
find_preorder(0, n-1, 0, n-1)

print(' '.join(map(str, preorder)))