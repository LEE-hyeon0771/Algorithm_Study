alpha = input().upper()
alpha_list = list(set(alpha))
answer = []

count = 0
for i in alpha_list:
    count = alpha.count(i)
    answer.append(count)

if answer.count(max(answer)) > 1:
    print("?")
else:
    print(alpha_list[answer.index(max(answer))])