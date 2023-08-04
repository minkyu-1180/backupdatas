# 9490. 풍선팡
import sys
sys.stdin = open("ballooninput.txt")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    max_c = 0
    for i in range(N):
        for j in range(M):
            c = arr[i][j]
            for l in range(4):
                for p in range(1, arr[i][j] + 1):
                    ni = i + p * di[l]
                    nj = j + p * dj[l]
                    if 0 <= ni < N and 0 <= nj < M:
                        c += arr[ni][nj]
            if max_c < c:
                max_c = c
    print(f'#{test_case} {max_c}')


'''

for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
    ni = i + di
    nj = j + dj
    
'''