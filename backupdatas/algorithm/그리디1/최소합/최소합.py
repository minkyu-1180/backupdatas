# sw academy 최소합
import sys
sys.stdin = open("최소합input.txt")

def go(i, j, c):
    global min_v

    if i == j == N-1:
        if min_v > c:
            min_v = c
    for di, dj in [[1, 0], [0, 1]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N:
            go(ni, nj, c + arr[ni][nj])


T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # 배열 크기(3 <= N <= 13)
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = arr[0][0]
    min_v = 10*10
    go(0, 0, result)
    print(f'#{test_case} {min_v}')
