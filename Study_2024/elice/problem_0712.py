'''
양의 정수로 이루어진 수열 a 
1
​
 ,a 
2
​
 ,⋯,a 
n
​
 이 있습니다.

1≤a 
i
​
 ≤10 
5
 
이 수열에서 각 원소를 선택하거나 선택하지 않음으로써 총 2 
n
 개의 부분 수열을 만들 수 있고, 만들어진 모든 부분 수열의 합인 2 
n
 개의 정수가 주어졌을 때, 원래의 수열 a 
1
​
 ,a 
2
​
 ,⋯,a 
n
​
 을 구하는 프로그램을 작성하세요.'''
 
import sys
from itertools import combinations

def dfs(res, x, sum_, now, m):
    if x == len(res):
        now.append(sum_ + m)
        return
    dfs(res, x + 1, sum_, now, m)
    dfs(res, x + 1, sum_ + res[x], now, m)

def solve():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    res = []
    now = []
    for i in range(1, len(v)):
        if v[i] not in now:
            m = v[i]
            dfs(res, 0, 0, now, m)
            res.append(v[i])
        now.remove(v[i])
    print(' '.join(map(str, res)))

if __name__ == "__main__":
    solve()