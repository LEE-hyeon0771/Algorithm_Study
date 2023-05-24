import sys
input = sys.stdin.readline

tree_kind = {}

count = 0
while True:
    name = input().rstrip()
    if not name:
        break
    if name in tree_kind:
        tree_kind[name] += 1     #전에 나온 경우 +1
    else:
        tree_kind[name] = 1      #처음 나온 경우 : 1대입

    count += 1      #변수 갯수 카운팅

tree = list(tree_kind.keys())
tree.sort()

for name in tree:
    print('%s %.4f' %(name, tree_kind[name]/count * 100))