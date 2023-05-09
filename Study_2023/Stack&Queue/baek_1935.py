N = int(input())
func = input()
alphabet = [0]*N

for i in range(N):
    alphabet[i] = int(input())

result = []

for i in func:
    if i.isalpha():
        result.append(alphabet[ord(i) - 65])
    else:
        str2 = result.pop()
        str1 = result.pop()

        if i == '+':
            result.append(str1 + str2)
        elif i == '-':
            result.append(str1 - str2)
        elif i == '*':
            result.append(str1 * str2)
        elif i == '/':
            result.append(str1 / str2)

print("%.2f" %result[0])

