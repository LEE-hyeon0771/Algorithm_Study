'''
강림제
시간 제한: 1초
코더 랜드에는 "엘리스"라는 신을 믿는 종교가 있습니다. 신실한 신도 체셔는 엘리스를 지상에
강림할 수 있게 해주는 강림제를 열려고 합니다. 체셔는 신도들에게 초대장을 돌리고, 초대장을 받은 신도들은 모두 자신이 언제 와서 언제 떠날 것인지 답변을 해주었습니다.

강림제가 시작되고 강림제에 참여 중인 사람들은 모두 기도를 시작합니다. 기도 중인 신도가 T명 이상이 되는 순간 엘리스가 지상에 강림하고 T명 미만이 되면 다시 사라진다고 합니다. 강림제를 담당하는 체셔는 기도 중인 신도가 T명 미만이 되면 엘리스가 강림하지 못한다는 것을 알고 급하게 자신의 친구 K명을 부르려고 합니다.

하지만 체셔의 친구들은 부끄러움이 많아서 체셔의 친구들을 제외한 신도가 T명 이상이 되는 순간 다 같이 강림제에서 나가 버리고 돌아오지 않는다고 합니다.
또한 기도 중인 인원이 T명 이상이면 체셔의 친구들은 강림제에 들어가지 않습니다.
단, 아직 들어가지 않은 체셔의 친구들은 이후 기도 인원이 T명 미만이 되면 강림제에 들어갈 수 있습니다.

체셔는 각각의 친구들을 적절한 시각에 강림제에 투입해 최대한 오랫동안 엘리스를 지상에 강림시키려고 합니다. 꼭 K명 모두 투입할 필요는 없습니다.

체셔는 엘리스를 얼마나 오랫동안 지상에 머물게 할 수 있는지 구하는 프로그램을 작성하세요.


지시사항
입력
첫째 줄에 강림제가 진행되는 시간 N, 강림제에 초대한 신도의 수 M, 체셔의 친구 수 K, 엘리스가 강림하기 위해 필요한 최소의 기도 인원 T를 입력합니다.
모든 입력은 자연수입니다.
1≤N,M,K≤300
1≤T≤M
둘째 줄부터 M개의 줄에 걸쳐 줄마다 a 
i
​
 , b 
i
​
 를 입력합니다. i번째 사람은 시각 a 
i
​
 에 기도에 참여하고, 시각 b 
i
​
 에 강림제를 떠납니다.
1≤a 
i
​
 ≤N
a 
i
​
 <b 
i
​
 ≤N+1
강림제가 시작되는 시각은 1을 기준으로 합니다.
출력
체셔의 친구들을 강림제에 투입했을 때 엘리스가 지상에 강림할 수 있는 최대 시간을 출력합니다.
입력 예시
11 3 2 2
3 12
5 10
7 8

출력 예시
9'''

import sys
input = sys.stdin.readline

def process_intervals(n, m, l, t, intervals):
    a = [0] * n
    for i, j in intervals:
        for k in range(i - 1, j - 1):
            a[k] += 1

    d = [0] * (l + 1)
    c = [0] * (t + 1)

    for i in range(n):
        if a[i] >= t:
            while len(c) > 1 and not c[-1]:
                c.pop()
            for i in range(len(c) - 1):
                c[i + 1] += c[i]
            d = [max(d[i - j] + c[j] for j in range(min(i + 1, len(c)))) + 1 for i in range(l + 1)]
            c = [0] * (t + 1)
        else:
            c[t - a[i]] += 1

    while len(c) > 1 and not c[-1]:
        c.pop()
    for i in range(len(c) - 1):
        c[i + 1] += c[i]
    d = [max(d[i - j] + c[j] for j in range(min(i + 1, len(c)))) for i in range(l + 1)]

    return d[-1]

    
n, m, l, t = map(int, input().split())
intervals = [tuple(map(int, input().split())) for _ in range(m)]
result = process_intervals(n, m, l, t, intervals)
print(result)
