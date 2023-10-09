import sys

n, k = map(int, input().split())
word = [set(input().rstrip()) for _ in range(n)]
learn = [False for _ in range(26)]
result = 0

def dfs(index, min_count):

    global result

    if min_count == k - 5:
        count = 0
        for i in word:
            flag = True
            for j in i:
                if not learn[ord(j) - 97]:
                    flag = False
                    break
            if flag:
                count += 1
        result = max(result, count)
        return
    for i in range(index, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, min_count + 1)
            learn[i] = False

if k < 5:
    print(0)
    exit(0)
elif k == 26:
    print(n)
    exit()
for i in ('a','c','i','n','t'):
    learn[ord(i) - 97] = True

dfs(0, 0)
print(result)

