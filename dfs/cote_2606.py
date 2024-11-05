# 웜 바이러스
# 연결 노드끼리 바이러스 전파.
# 첫째줄 : 컴퓨터의 수 (N)
# 둘째줄 : 직접 연결되어 있는 컴퓨터 쌍의 수 (M)
# 나머지 : 한 쌍씩 연결 정보

# 1. N, M 입력 받아서 adj[[] for _ in range(N+1)] 생성
# 2. M을 통해서 for문 구성, 나머지 정보들 연결 리스트 생성 adj[?] 정보 삽입
# 3. ans_dfs = [], v = [0]*(N+1)
# 4. 방문하면 v[c] = 1, ans_dfs.append(c)
# 5. 방문 안했을 경우, 방문하여 방문처리 및 정답 리스트에 추가
# 6. 1번 컴퓨터를 통해 감염된 컴퓨터의 수를 출력하는 것이므로, print(len(ans_dfs)-1)

N = int(input())
M = int(input())

adj = [[] for _ in range(N+1)]

for i in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

for i in range(N+1):
    adj[i].sort()

def dfs(c):
    v[c] = 1
    ans_dfs.append(c)

    for i in adj[c]:
        if v[i] == 0:
            dfs(i)

ans_dfs = []
v = [0]*(N+1)

dfs(1)

print(len(ans_dfs)-1)
