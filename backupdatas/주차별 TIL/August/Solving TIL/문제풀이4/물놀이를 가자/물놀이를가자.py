# sw academy 물놀이를 가자
import sys
sys.stdin = open('물놀이input.txt')

'''
# 물놀이2
def min_dist(i, j):
    global min_c

    if arr[i][j] == 'W':
        if min_c > visited[i][j] - 1:
            min_c = visited[i][j] - 1
        # visited[i][j] = 0
    else:
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nr, nc = i + di, j + dj
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                visited[nr][nc] = visited[i][j] + 1
                min_dist(nr, nc)
                visited[nr][nc] = 0

T = int(input())
for test_case in range(1, T+1):
    # N x M 문자열 (1 <= N, M <= 1000)
    N, M = map(int, input().split())

    # 각 원소 : W or L(W : Water / L : Land)
    arr = [input() for _ in range(N)]

    # 땅 인덱스 찾기
    land_idx = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'L':
                land_idx.append((i, j))

		result = 0
    for i, j in land_idx:
        min_c = 1000000
        visited = [[0] * M for _ in range(N)]
        visited[i][j] = 1
				min_dist(i, j)

        result += min_c


    print(f'#{test_case} {result}')
'''

'''
# 물놀이1
T = int(input())
for test_case in range(1, T+1):
    # N x M 문자열 (1 <= N, M <= 1000)
    N, M = map(int, input().split())

    # 각 원소 : W or L(W : Water / L : Land)
    arr = [input() for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]    
    # 땅 인덱스 찾기
    land_idx = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'L':
                land_idx.append((i, j))
    # 각 땅에서 물로 이동하기 위한 최소값을 구하고, 모든 최소값들의 합 구하기
    result = 0
    for start in land_idx:
        min_c = 1000**2
        y, x = start
        c = 1
        que = [[[y, x]]]

        while que:
            now = que.pop(0)
            i, j = now[0][0], now[0][1]

            for k in range(4):
                nr, nc = i + di[k], j + dj[k]
                if 0 <= nr < N and 0 <= nc < M:
                    c += 1
                    if arr[nr][nc] == 'W' and c - 1 < min_c:
                        min_c = c - 1
                    elif arr[nr][nc] == 'L':
                        new = [[nr, nc]] + now
                        que.append(new)

        result += min_c

    print(f'#{test_case} {result}')
'''

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
        result += visited[cr][cc]
        for i in range(4):
            nr, nc = cr + di[i], cc + dj[i]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == -1:
                visited[nr][nc] = visited[cr][cc] + 1
                que.append([nr, nc])

    print(f'#{test_case} {result}')

