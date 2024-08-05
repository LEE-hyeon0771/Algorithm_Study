import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

def plug(N, K, usage):
    plugged_in = []
    count = 0
    
    for i in range(K):
        if arr[i] in plugged_in:
            continue
        if len(plugged_in) < N:
            plugged_in.append(arr[i])
        else:
        
            far = -1
            temp = -1
            for plug in plugged_in:
                if plug not in arr[i:]:
                    temp = plug
                    break
                elif arr[i:].index(plug) > far:
                    far = arr[i:].index(plug)
                    temp = plug
        
            plugged_in[plugged_in.index(temp)] = arr[i]
            count += 1
    return count

print(plug(N, K, arr))