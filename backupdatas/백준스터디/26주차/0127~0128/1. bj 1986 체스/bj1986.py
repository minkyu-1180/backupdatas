# 백준 1986. 체스
import sys
sys.stdin = open("bj1986input.txt")
# 원래 T는 없음
T = int(input())
for tc in range(T):

    N, M = map(int, input().split())
    queens = list(map(int, input().split()))
    knights = list(map(int, input().split()))
    pawns = list(map(int, input().split()))

    # arr = [['' for _ in range(M)] for _ in range(N)]
    arr = [[0] * M for _ in range(N)]
    q = queens[0]
    for i in range(1, 2*q+1, 2):
        y = queens[i] - 1
        x = queens[i+1] - 1
        arr[y][x] = 1

    k = knights[0]
    for i in range(1, 2*k+1, 2):
        y = knights[i] - 1
        x = knights[i+1] - 1
        arr[y][x] = 2

    p = pawns[0]
    for i in range(1, 2*p+1, 2):
        y = pawns[i] - 1
        x = pawns[i+1] - 1
        arr[y][x] = 3

    dir_q = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
    dir_k = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]

    result = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                result[i][j] += 1
                for di, dj in dir_q:
                    for k in range(1, max(N, M)):
                        ni = i + k * di
                        nj = j + k * dj
                        if not (0 <= ni < N and 0 <= nj < M) or arr[ni][nj]:
                            break
                        result[ni][nj] += 1

            elif arr[i][j] == 2:
                result[i][j] += 1
                for di, dj in dir_k:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                        result[ni][nj] += 1

            elif arr[i][j] == 3:
                result[i][j] += 1
    res = 0
    for i in range(N):
        for j in range(M):
            if result[i][j] == 0:
                res += 1
    print(res)