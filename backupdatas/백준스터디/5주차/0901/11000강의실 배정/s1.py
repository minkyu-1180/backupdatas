
from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    que = deque()
    visited = [[-1] * M for _ in range(N)]
    # 물인거만 담는다.
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 'W':
                que.append([r, c])
                visited[r][c] = 0
    result = 0
    while que:
        cr, cc = que.popleft()
        cnt = visited[cr][cc]
        result += visited[cr][cc]
        for i in range(4):
            nr, nc = cr + di[i], cc + dj[i]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == -1:
                visited[nr][nc] = visited[cr][cc] + 1
                que.append([nr, nc])

    print(f'#{test_case} {result}')