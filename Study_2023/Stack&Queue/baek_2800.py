from itertools import combinations

n = list(input())

stack = []       #stack리스트
temp = []        #result로 넘기기 전에 담아두는 리스트
result = set()   #최종결과 - 중복제거를 위해 set으로

for i in range(len(n)):
    if n[i] == '(':               #'(" 나오면 stack에 담기
        stack.append(i)
    elif n[i] == ')':             #')' 나오면 stack에서 pop 시켜서 그대로 temp 리스트에 잠시 담아둠.
        temp.append((stack.pop(), i))

for i in range(1, len(temp) + 1):       #temp 리스트에서 가능한 조합들을 찾기
    comb = list(combinations(temp, i))

    for j in comb:                      #문자열을 다시 그대로 복사
        copy_str = list(n)
        for x,y in j:
            copy_str[x] = ''            #x,y가 조합에 있을 때, 공백 넣기
            copy_str[y] = ''

        result.add(''.join(copy_str))     #조합값을 합쳐서 result 리스트에 담기

result = list(result)                 #다시 list로 바꾸어주고 sorting 정렬
result.sort()

for i in result:
    print(i)