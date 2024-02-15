import sys
input = sys.stdin.readline

n = int(input())
result = []

def backtracking(count):
    if count == n:
        print(''.join(map(str, result)))
        return True

    for i in range(1, 4):
        result.append(i)
        
        isGood = True
        for cut in range(1, (len(result) // 2) + 1):
            if result[-cut:] == result[-2*cut:-cut]:
                isGood = False
                break

        if isGood:
            if backtracking(count + 1):
                return True
        result.pop()
    return False

backtracking(0)
        
                