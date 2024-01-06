# 백준 30679. 별 가두기
import sys
sys.stdin = open("bj30679input.txt")


def star(arr, i, j):
    '''
    visited를 어떻게 표현해야 할까요?

    '''
    visited = dict()
    for r in range(N):
        for c in range(M):
            visited[(r, c)] = [0, 0, 0, 0]
    # print(visited)
    d = 0

    while True:
        val = arr[i][j]
        di, dj = dir[d]
        ni = i + di * val
        nj = j + dj * val
        # 다음에 갈 위치가 나가야하면
        if (0 > ni or ni >= N) or (0 > nj or nj >= M):
            return False
        if visited[(i, j)][d] == 1:
            return True
        visited[(i, j)][d] = 1

        d = (d+1)%4
        i, j = ni, nj



# 원래 T는 없음
T = int(input())
for tc in range(T):
    # N : 장치의 세로 길이(1 <= N <= 100)
    # M : 장치의 가로 길이(1 <= M <= 100)
    N, M = map(int, input().split())

    # arr
    arr = [list(map(int, input().split())) for _ in range(N)]


    '''
    1. 첫 번째 열의 원하는 칸에 별을 올려둔다
    2. 다음과 같은 과정을 따라 별이 이동한다
    - 1. 별은 바라보고 있는 방향으로, 별이 놓인 칸에 적힌 수만큼 이동한다
    - 2. 별이 바라보는 방향이 시계 방향으로 90도 돌아간다
    * 별은 처음에 오른쪽을 바라보고 있음
    '''
    dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    # star(arr, 1, 0)
    result = [0] * N
    for i in range(N):
        if star(arr, i, 0):
            result[i] = 1
    if result.count(1):
        print(result.count(1))
        for i in range(N):
            if result[i]:
                print(i+1, end=' ')
        print()
    else:
        print(0)