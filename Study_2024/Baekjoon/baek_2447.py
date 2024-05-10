import sys
input = sys.stdin.readline

n = int(input())

def star(n):
    if n == 1:
        return ["*"]
    
    sub_n = n // 3
    sub_star = star(sub_n)
    
    result = []
    
    for i in range(3):
        for j in range(sub_n):
            if i == 1:
                result.append(sub_star[j] + ' ' * sub_n + sub_star[j])
            else:
                result.append(sub_star[j] * 3)
    
    return result

print(*star(n))
    
    