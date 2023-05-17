parenthesis = list(input())
stack = []
temp = 1
result = 0

for i in range(len(parenthesis)):
    if parenthesis[i] == "(":
        temp *= 2
        stack.append("(")
    elif parenthesis[i] == "[":
        temp *= 3
        stack.append("[")

    elif parenthesis[i] == ")":                   # ")"를 만난 상황
        if not stack or stack[len(stack)-1] == "[":        # 1. 앞이 "["일 때(비정상)
            result = 0
            break
        if parenthesis[i-1] == "(":               # 2. 앞이 "("일 때(정상)
            result += temp
        temp = temp // 2
        stack.pop()

    else:                                         # "]"를 만난 상황
        if not stack or stack[len(stack)-1] == "(":        # 1. 앞이 "("일 때(비정상)
            result = 0
            break
        if parenthesis[i-1] == "[":               # 2. 앞이 "["일 때(정상)
            result += temp
        temp = temp // 3
        stack.pop()

if stack:
    print(0)
else:
    print(result)


