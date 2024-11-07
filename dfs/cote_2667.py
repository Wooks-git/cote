def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:  # 범위 체크 먼저
        return
    if V[x][y] == 1 or adj[x][y] == 0:  # 이미 방문했거나 집이 없는 경우. 즉, dfs를 수행하면서 집이 없거나, 방문일 경우는 원점으로 돌아오는것.
        return

    V[x][y] = 1  # 방문 표시
    global cnt
    cnt += 1

    for _ in range(4):
        nx = x + dx[_]
        ny = y + dy[_]
        dfs(nx, ny)  # 이동

N = int(input())  # 한 변의 길이
adj = [list(map(int, input())) for _ in range(N)]
V = [[0] * N for _ in range(N)]
ans = []

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(N):
    for j in range(N):
        if adj[i][j] == 1 and V[i][j] == 0:
            cnt = 0
            dfs(i, j)
            ans.append(cnt)

ans.sort()
print(len(ans))
print(*ans, sep='\n')
