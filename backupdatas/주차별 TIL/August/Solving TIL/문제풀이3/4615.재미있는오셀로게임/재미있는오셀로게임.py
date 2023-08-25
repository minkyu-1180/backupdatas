# 재미있는 오셀로 게임
import sys
sys.stdin = open("재미있는오셀로게임input.txt")

bosaek = {1 : 2,
          2 : 1}
dir = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
def func(i, j, color, N):
    arr[i][j] = color # 해당 위치에 돌 놓기
    # 빈칸 / 영역 밖 -> 종료
    for di, dj in dir:
        ni = i + di
        nj = j + dj
        tmp = []
        while 1 <= ni <= N and 1 <= nj <= N and arr[ni][nj] == bosaek[color]:
            tmp.append((ni, nj))
            ni, nj = ni + di, nj + dj
        if 1 <= ni <= N and 1 <= nj <= N and arr[ni][nj] == color:
            for y, x in tmp:
                arr[y][x] = color


T = int(input())
for test_case in range(1, T+1):
    # N : 한 변의 길이(4, 6, 8)
    # M : 플레이어가 돌을 놓는 횟수
    N, M = map(int, input().split())
    arr = [[0] * (N+1) for _ in range(N+1)]
    arr[N//2][N//2] = arr[N//2+1][N//2+1] = 2
    arr[N//2][N//2+1] = arr[N//2+1][N//2] = 1

    # 방향(8가지)

    # 흑 : 1 / 백 : 2
    for _ in range(M):
        j, i, color = map(int, input().split())
        func(i, j, color, N)

    b_c = w_c = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == 1:
                b_c += 1
            elif arr[i][j] == 2:
                w_c += 1
    print(f'#{test_case} {b_c} {w_c}')