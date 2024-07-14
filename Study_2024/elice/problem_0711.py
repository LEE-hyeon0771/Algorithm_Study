'''
정점 N개의 트리에서 두 사람이 게임을 진행하려 한다.
각 정점은 1번부터 N번 까지 번호가 매겨져 있고 루트노드는 1번 노드이다.
게임은 서로 턴을 번갈아 가며 진행되고 트리 위에 놓을 수 있는 말과 함께 진행된다.
두 사람의 점수는 모두 0점으로 시작한다.

각 턴마다 두 사람은 다음과 같은 작업을 반복한다.

현재 말이 놓여 있는 정점의 번호만큼 자신의 점수에 더한다.
현재 말이 놓여 있는 정점의 자식 정점이 없다면 그대로 게임을 종료한다.
자식 정점이 존재한다면 자식 정점 중 원하는 자식 정점으로 말을 옮긴다.
게임이 종료되었을 때 선공의 점수가 후공의 점수보다 높거나 같다면 선공이 승리하고 아니라면 후공이 승리한다.
두 사람이 최적으로 플레이할 때, 처음 말이 놓여져 있는 정점의 번호에 따라 선공이 이기는지 후공이 이기는지 구해보자.





외부에서 작성한 코드를 복사 및 붙여넣기 시, 정확한 코드 작성 시간 산정이 힘들어 수상 과정에서 불이익이 발생할 수 있습니다. 이는 운영진 측에서 확인이 가능한 사항이므로, 모든 코드는 엘리스 플랫폼 내에서 작성을 부탁드립니다.


또한, ChatGPT나 생성 AI, 외부 API 사용 시 수상에서 불이익을 받을 수 있다는 점도 같이 참고 부탁드립니다.


입력
첫째 줄에 정점의 수 N이 주어진다.
1≤N≤100000
둘째 줄부터 N−1개의 줄에 간선을 나타내는 정수 u,v가 주어진다.
1≤u,v≤N
이는 u번 정점과 v번 정점을 잇는 간선이 존재한다는 뜻이다.
출력
N개의 줄에 걸쳐 정답을 출력한다.
i번째 줄에는 말의 시작위치가 i번 정점일 때의 결과를 출력한다.
선공이 이긴다면 1을 후공이 이긴다면 0을 출력한다.
입력 예시 1
5
1 3
2 1
3 4
5 1
Copy
출력 예시 1
1
1
0
1
1
Copy
입력 예시 2
6
1 3
1 2
3 5
3 6
2 4
Copy
출력 예시 2
1
0
0
1
1
1'''

from collections import defaultdict

v=defaultdict(list)
dp=[None]*100050
inf=int(1e12)

def dfs(x:int ,par:int):
    global dp,v
    
    ret=inf
    
    for nxt in v[x]:
        if nxt==par:
            continue
            
        dfs(nxt,x)
        ret=min(ret,dp[nxt])
        
    if ret==inf:
        ret=0
        
    dp[x]=x-ret

n=int(input())

for _ in range(1,n):
    a,b=(map(int,input().split()))
    v[a].append(b)
    v[b].append(a)

dfs(1, 0)

for i in range(1,n+1):
    print('1' if dp[i]>=0 else '0')