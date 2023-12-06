# 백준 14499. 주사위 굴리기
import sys
sys.stdin = open("bj14499input.txt")
from copy import deepcopy
# 원래 T는 없음
T = int(input())
for tc in range(T):
    # N, M : 지도의 세로, 가로 크기(1 <= N, M <= 20)
    # x, y : 주사위를 놓은 곳의 좌표(0 <= x <= N-1, 0 <= y <= M-1)
    # K : 명령어 개수(1 <= K <= 1000)
    N, M, x, y, K = map(int, input().split())

    # 지도에 쓰여있는 수
    # arr[i][j] : 0 ~ 9
    # 주사위를 놓은 칸에 쓰여있는 수는 항상 0
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 명령이 순서대로 주어짐
    # 동쪽 : 1 / 서쪽 : 2 / 북쪽 : 3 / 남쪽 : 4
    commands = list(map(str, input().split()))


    '''
    주사위
        2
      4 1 3
        5
        6
    시작 상황 : 지도 위에 윗 면이 1이고, 동쪽을 바라보는 방향이 3인 상태
    # 위 동 서 북 남 아래
    [1, 3, 4, 2, 5, 6]
    1. 동쪽으로 이동시
        2
      6 4 1
        5
        3
    [4, 1, 6, 2, 5, 3]
    2. 서쪽으로 이동시
        2
      1 3 6
        5
        4
    [3, 6, 1, 2, 5, 4]
    3. 북쪽으로 이동시
        1
      4 5 3
        6
        2
    [5, 3, 4, 1, 6, 2]
    4. 남쪽으로 이동시
        6
      4 2 3
        1
        5
    [2, 3, 4, 6, 1, 5]
    '''
    # [1, 3, 4, 2, 5, 6]
    def change_dice(dir, ni, nj):
        global dice

        # dice 방향
        u, e, w, n, s, d = dice
        if dir == [0, 1]:
            dice = [w, u, d, n, s, e]
        elif dir == [0, -1]:
            dice = [e, d, u, n, s, w]
        elif dir == [-1, 0]:
            dice = [s, e, w, u, d, n]
        elif dir == [1, 0]:
            dice = [n, e, w, d, u, s]

        dice_down = deepcopy(dice[5])
        now = deepcopy(arr[ni][nj])
        if now == 0:
            arr[ni][nj] = dice_down
        else:
            dice[5] = now
            arr[ni][nj] = 0


    dictionary = {
        '1' : [0, 1],
        '2' : [0, -1],
        '3' : [-1, 0],
        '4' : [1, 0],
    }
    # dice[0] : 현재 위
    # dict[5] : 현재 바닥

    # 주사위 시작 상황
    # u, e, w, n, s, d
    dice = [0, 0, 0, 0, 0, 0]
    # 주사위 현재 위치
    now = (x, y)
    for k in range(K):
        i, j = now
        cmd = commands[k]
        dir = dictionary[cmd]
        ni = i + dir[0]
        nj = j + dir[1]
        # 명령어 실행 시 지도 안에 있을 경우만 진행
        if 0 <= ni < N and 0 <= nj < M:
            now = (ni, nj)
            change_dice(dir, ni, nj)
            # print(dice)
            print(dice[0])

    # print()