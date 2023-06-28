N = int(input())
loss = list(map(int, input().split()))
loss.sort()

result = loss[-1]
if N % 2 == 1:
    for i in range(N//2):
        temp = loss[i] + loss[N-i-2]   # i=0, 5-0-2 = 3 -> index 3 : 4
        if result < temp:
            result = temp

else:
    for i in range(N//2):
        temp = loss[i] + loss[N-i-1]
        if result < temp:
            result = temp

print(result)