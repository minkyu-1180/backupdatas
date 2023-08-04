# 16268. 풍선팡 2
import sys
sys.stdin = open("balloon2input.txt")

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 오른쪽 +1 / 왼쪽 +1 / 아래로 +1 / 위로 +1
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    max_c = 0
    result = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            c = arr[i][j]
            for l in range(4):
                ni = i + di[l]
                nj = j + dj[l]
                if 0 <= ni <= N-1 and 0 <= nj <= M-1:
                    c += arr[ni][nj]
            result[i][j] = c
            if max_c < c:
                max_c = c

    print(f'#{test_case} {max_c}')
