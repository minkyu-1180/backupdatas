# 백준 21610. 마법사 상어와 비바라기
import sys
sys.stdin = open("bj21610input.txt")

# 원래 T는 없음
T = int(input())
for tc in range(T):
    # N : 행, 열의 개수 (2 <= N <= 50)
    # M : 명령의 개수 (1 <= M <= 100)
    N, M = map(int, input().split())

    # arr[i][j] : (i, j)에 들어있는 물의 양양
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 비구름 초반 위치 : (N, 1), (N, 2), (N-1, 1), (N-1, 2)
    clouds_now = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
    dir8 = [[0, 0], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
    dir4 = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
    for _ in range(M):
        # visited[i][j] : 해당 칸이 3번 로직에서 구름이 사라진 칸인지에 대한 여부
        visited = [[0] * N for _ in range(N)]
        # 이동한 구름 좌표(겹치는 애들 존재 가능할 수도 있어서 set으로
        bug_idx = set()
        # 1. 모든 구름이 di방향으로 si칸 이동한다.
        d, s = map(int, input().split())
        for i in range(len(clouds_now)):
            y, x = clouds_now[i]
            dy = dir8[d][0]
            dx = dir8[d][1]
            ny = (y+dy*s)%N
            nx = (x+dx*s)%N

            # 2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니가 저장된 물의 양이 1 증가한다.
            arr[ny][nx] += 1
            bug_idx.add((ny, nx))
            if visited[ny][nx] == 0:
                visited[ny][nx] = 1
        # 3. 구름이 모두 사라진다.
        clouds_next = []
        # 4. 2에서 물이 증가한 칸에 물복사버그 마법 시전
        for i, j in list(bug_idx):

            for di, dj in dir4:
                ni = i + di
                nj = j + dj
                # 대각선 인접 칸이 존재 & 해당 칸에 물이 있을 경우, (i, j)에 +1
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj]:
                    arr[i][j] += 1
        # 5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다
        # 이 때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
        for i in range(N):
            for j in range(N):
                if arr[i][j] >= 2 and visited[i][j] == 0:
                    clouds_next.append((i, j))
                    arr[i][j] -= 2
        clouds_now = clouds_next
    result = 0
    for i in range(N):
        for j in range(N):
            result += arr[i][j]
    print(result)



