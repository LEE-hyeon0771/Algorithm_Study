import sys
input = sys.stdin.readline

T = int(input())
arr = [list(map(int, input().split())) for _ in range(T)]

def find_decimal(num, denominator):
    result = []
    map = {}
    
    integer_part = num // denominator
    result.append(str(integer_part))
    remainder = num % denominator
    if remainder == 0:
        result.append('.(0)')
        return ''.join(result)
    
    result.append('.')
    index = len(result)
    
    while remainder != 0:
        if remainder in map:
            insert_position = map[remainder]
            result.insert(insert_position, '(')
            result.append(')')
            break
        map[remainder] = index
        remainder *= 10
        result.append(str(remainder // denominator))
        remainder %= denominator
        index += 1
        
    if remainder == 0 and '(' not in result:
        result.append('(0)')

    return ''.join(result)

results = [find_decimal(num, denominator) for num, denominator in arr]

for result in results:
    print(result)
