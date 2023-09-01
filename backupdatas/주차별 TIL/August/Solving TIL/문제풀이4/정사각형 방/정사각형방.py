# sw academy 정사각형 방
import sys
sys.stdin = open("정사각형input.txt")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_c = 0
    max_start = 0

    for y in range(N):
        for x in range(N):
            i, j = y, x
            c = 1
            start = arr[i][j]

            while True:
                for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] - arr[i][j] == 1:
                        c += 1
                        i, j = ni, nj
                        break
                else:
                    break
            if max_c < c:
                max_c = c
                max_start = start
            elif max_c == c and max_start > start:
                max_start = start
    print(f'#{test_case} {max_start} {max_c}')

# 두 번째 방법
    cnt = [0] * (N * N + 1) # 0 ~ N*N번까지(연속으로 1이 커지는 경우를 표시할 배열
    for i in range(N):
        for j in range(N):
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] - arr[i][j] == 1:
                    cnt[arr[i][j]] = 1

    max_c = 0
    max_s = 0

    c = 0
    for k in range(N*N, 0, -1):
        if cnt[k] == 1:
            c += 1
            max_c = c
            max_s = k
        elif max_c == c:
            max_s = k

        else:
            c = 0
