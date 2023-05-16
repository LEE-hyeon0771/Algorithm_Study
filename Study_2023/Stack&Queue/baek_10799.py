stick = list(input())
answer = []
count = 0

for i in range(len(stick)):
    if stick[i] == '(':
        answer.append("(")

    else:
        if stick[i-1] == "(":
            answer.pop()
            count += len(answer)
        else:
            answer.pop()
            count += 1

print(count)