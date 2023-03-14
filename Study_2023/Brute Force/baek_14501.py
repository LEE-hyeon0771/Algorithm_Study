def Max_profit(day, profit):
    global sum

    if day > N + 1:
        return
    if day == N + 1:
        sum = max(sum, profit)
        return
    Max_profit(day + T[day], profit + P[day])
    Max_profit(day + 1, profit)


N = int(input())

T = [0] * (N + 1)
P = [0] * (N + 1)

for i in range(1, N + 1):
    T[i], P[i] = map(int, input().split())

sum = 0

Max_profit(1, 0)
print(sum)