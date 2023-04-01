S = int(input())

n = 0
sum = 0

while True:
    sum += n;
    if sum > S:
        break;
    n = n + 1

print(n-1)
