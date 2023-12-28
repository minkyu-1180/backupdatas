# 백준 17144. 미세먼지 안녕!

import sys
sys.stdin = open("bj17144input.txt")

def misemungi():
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    change = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                c = 0
                how = arr[i][j]//5
                for di, dj in dir:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] != -1:
                        change[ni][nj] += how
                        c += 1
                change[i][j] -= c * how
    for i in range(R):
        for j in range(C):
            arr[i][j] += change[i][j]
    return

def clean1():
    dir = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    direction = 0
    last = 0

    # 현재 공기청정기 위치
    i, j = cleaners[0][0], 1

    start = cleaners[0]

    i, j = cleaners[0][0], 1
    while True:
        # 시작 위치로 되돌아왔으면 끝
        if (i, j) == cleaners[0]:
            break
        di, dj = dir[direction]
        ni = i + di
        nj = j + dj
        # 범위 문제 확인
        if ni < 0 or ni >= R or nj < 0 or nj >= C:
            direction = (direction+1)%4
            continue
        # 범위 문제 없으면 갱신 후 이동
        arr[i][j], last = last, arr[i][j]
        i = ni
        j = nj
    return


def clean2():
    dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    direction = 0
    last = 0

    # 현재 공기청정기 위치
    start = cleaners[1]

    i, j = cleaners[1][0], 1
    while True:
        # 시작 위치로 되돌아온 경우 끝
        if (i, j) == cleaners[1]:
            break
        di, dj = dir[direction]
        ni = i + di
        nj = j + dj

        # 범위 벗어나면 방향 바꾸고 다시 진행
        if ni < 0 or ni >= R or nj < 0 or nj >= C:
            direction = (direction+1)%4
            continue

        # 범위 문제 없으면 갱신 후 이동
        arr[i][j], last = last, arr[i][j]
        i = ni
        j = nj
    return

T = int(input())
for tc in range(T):
    # R, C : 주어진 행, 열 크기(6 <= R, C <= 50)
    # TIME : 주어진 시간(1 <= T <= 1000)
    R, C, TIME = map(int, input().split())
    arr = []
    cleaners = [] # 두 공기청정기 위치
    for i in range(R):
        lst = list(map(int, input().split()))
        if lst[0] == -1:
            cleaners.append((i, 0))
        arr.append(lst)

    t = 0
    while t < TIME:
        misemungi()
        clean1()
        clean2()
        t += 1
    result = 0
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                result += arr[i][j]
    print(result)