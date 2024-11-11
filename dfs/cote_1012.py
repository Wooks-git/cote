# 유기농 배추
# 지렁이 : 배추 근처에서 해충 잡아먹음
# 인접 배추들은 해당 지렁이로부터 보호 받을 수 있음.
# 인접 : 상하좌우 네 방향에 인접할 경우
# 배추밭에 최소 몇마리의 지렁이가 필요한지

# 첫째줄 : 테스트 케이스 T
# 둘째줄 : 각 테스트에 대해 가로 (M), 세로 (N), 배추 개수 (K)
# 그 후는 배추 위치 정보

# T를 입력 받아서, T만큼 for문
# 그 for문 안에서 M, N, K 입력 받기
# 입력받은 M, N을 이용해서 MxN 행렬 만들기 (arr, v) arr : 배추 맵, v : visitied
# 그 후 K번의 for문을 통해 배추 위치로 arr에 1 삽입
# MxN만큼 for문 돌면서 1나오면 dfs로 확인하여 visited 채우기
# dfs 빠져나오면 배추간의 연결이 끊어졌다는 뜻이므로, warm_count += 1을 해줌.
# print(warm_count)

def dfs(m, n):
    if m < 0 or m >= M or n < 0 or n >= N:  # 범위를 벗어나면 종료
        return
    if arr[m][n] == 0 or V[m][n] == 1:  # 배추가 없거나 이미 방문했다면 종료
        return

    V[m][n] = 1  # 방문 표시

    for l in range(4):  # 네 방향으로 DFS 탐색
        x = m + dx[l]
        y = n + dy[l]
        dfs(x, y)

T = int(input())  # 테스트 케이스 수

# 위, 아래, 좌, 우 방향 이동
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for t in range(T):
    M, N, K = map(int, input().split())  # 배추밭의 크기와 배추 위치 수
    arr = [[0] * N for _ in range(M)]
    V = [[0] * N for _ in range(M)]

    # 배추 위치 입력 받기
    for _ in range(K):
        b_i, b_j = map(int, input().split())
        arr[b_i][b_j] = 1

    worm_count = 0  # 현재 테스트 케이스의 지렁이 수

    for i in range(M):
        for j in range(N):
            if arr[i][j] == 1 and V[i][j] == 0:  # 배추가 있고 방문하지 않았다면
                dfs(i, j)  # DFS를 통해 연결된 배추 탐색
                worm_count += 1  # 배추흰지렁이 수 증가

    print(worm_count)  # 각 테스트 케이스의 배추흰지렁이 수 출력
