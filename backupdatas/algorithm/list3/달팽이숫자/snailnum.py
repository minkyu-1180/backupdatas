# sw academy - 1954. 달팽이 숫자
import sys
sys.stdin = open("snailnuminput.txt")
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    # 우, 하, 좌, 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    arr = [[0] * N for _ in range(N)]
    # print(arr)

    # 달팽이가 이동할 때 값을 증가시키고 기록할 변수
    c = 1
    # 시작 좌표 설정
    x, y = 0, 0
    # 이동 방향
    direction = 0
    # 시작 위치에 1 기록
    arr[x][y] = c

    # 반복 시작
    while c < N ** 2:
        nx = x + dx[direction] # nx = x + 0
        ny = y + dy[direction] # ny = y + 1

        # 다음 조사 위치가 0보다 크거나 같고 N보다 작으면
        # 동시에 다음 위치가 기록되지 않은 곳이면(즉, 0이면)
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
            c += 1
            # 해당 index에 숫자 기입
            arr[nx][ny] = c
            # 현재 위치 갱신
            x, y = nx, ny
        else:
            direction = (direction + 1) % 4

    print(f'#{test_case}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = ' ')
        print()

