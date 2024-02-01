import sys
input = sys.stdin.readline

n = int(input())
moves = []

def hanoi(n, from_pos, aux_pos, to_pos):
    if n == 1:
        moves.append(f"{from_pos} {to_pos}")
        return
    
    hanoi(n-1, from_pos, to_pos, aux_pos)
    moves.append(f"{from_pos} {to_pos}")
    hanoi(n-1, aux_pos, from_pos, to_pos)

if n <= 20:
    hanoi(n, 1, 2, 3)

print(2 ** n-1)
for move in moves:
    print(move)