import sys

input = sys.stdin.readline

def back_traking(count, index):
    if count == L:
        consonant = 0
        vowel = 0

        for i in range(L):
            if result[i] in con_list:
                vowel += 1
            else:
                consonant += 1

        if vowel >= 1 and consonant >= 2:
            print("".join(result))
        return

    for i in range(index, C):
        result.append(alpha[i])
        back_traking(count + 1, i + 1)
        result.pop()

L, C = map(int, input().split())
alpha = list(map(str, input().split()))
alpha.sort()
con_list = ['a', 'e', 'i', 'o', 'u']
result = []
back_traking(0, 0)



