# weights 배열 내의 값의 누적값을 다음 누적값이 넘어버릴 경우 stop


import sys
input = sys.stdin.readline

def fine_weight(weights):
    weights.sort()
    min_weight = 1
    
    for weight in weights:
        if weight <= min_weight:
            min_weight += weight
        else:
            break

    return min_weight

n = int(input())
arr = list(map(int, input().split()))

result = fine_weight(arr)
print(result)