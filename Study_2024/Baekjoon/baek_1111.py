# n이 1이면, 다 똑같아서 수가 여러개임 -> A 출력
# n이 2이면, 앞 뒤가 같을 경우에는 앞 수 그냥 출력, 다르면 수가 여러개 올 수 있어서 A 출력 
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

if n == 1:
    print('A')
elif n == 2:
    if arr[0] == arr[1]:
        print(arr[0])
    else:
        print('A')

else:
    if arr[0] == arr[1]:
        a = 0
        b = arr[0]
    else:
        a = (arr[1] - arr[2]) // (arr[0] - arr[1])
        b = arr[1] - arr[0] * a

    for i in range(n - 1):
        if(arr[i + 1] != (arr[i]*a + b)):   # 다음 수가 예측 안될 때 B 출력
            print('B')
            sys.exit(0)
    print(arr[-1] * a + b)