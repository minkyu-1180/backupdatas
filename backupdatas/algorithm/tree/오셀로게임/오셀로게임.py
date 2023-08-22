# sw academy 오셀로게임
import sys
sys.stdin = open("오셀로input.txt")

T = int(input())
for test_case in range(1, T+1):
    # N : 보드의 한 변(4, 6, 8)
    # M : 플레이어가 돌을 놓는 횟수
    N, M = map(int, input().split())
    arr = [[0] * (N+1) for _ in range(N+1)]

    # 초기 상태 설정
    m = N//2
    arr[m][m] = arr[m+1][m+1] = 2 # 백
    arr[m][m+1] = arr[m+1][m] = 1 # 흑

    delta = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

    for _ in range(M):
        j, i, color = map(int, input().split())

        for d in delta:
            for l in range(N, 1, -1):
                ni = i + d[0] * l
                nj = j + d[1] * l
                if 1 <= ni < N+1 and 1 <= nj < N+1:
                    if arr[ni][nj] == color:
                        for k in range(1, l):
                            if arr[i + k * d[0]][j + k * d[1]] == 0:
                                break
                        else:
                            for k in range(l):
                                arr[i + k * d[0]][j + k * d[1]] = color
                            break


    b_count = 0
    w_count = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == 1:
                b_count += 1
            if arr[i][j] == 2:
                w_count += 1
    print(f'#{test_case} {b_count} {w_count}')

'''
T = int(input())
for test_case in range(1, T+1):
    # N : 보드의 한 변(4, 6, 8)
    # M : 플레이어가 돌을 놓는 횟수
    N, M = map(int, input().split())
    arr = [[0] * (N+1) for _ in range(N+1)]

    # 초기 상태 설정
    m = N//2
    arr[m][m] = arr[m+1][m+1] = 2 # 백
    arr[m][m+1] = arr[m+1][m] = 1 # 흑

    delta = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

    for _ in range(M):
        j, i, color = map(int, input().split())

        for d in delta:
            for l in range(N, 0, -1):
                ni = i + d[0] * l
                nj = j + d[1] * l
                if 1 <= ni < N+1 and 1 <= nj < N+1:
                    if arr[ni][nj] == color:
                        for k in range(l):
                            arr[i + k * d[0]][j + k * d[1]] = color
                        break


    b_count = 0
    w_count = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == 1:
                b_count += 1
            if arr[i][j] == 2:
                w_count += 1
    print(f'#{test_case} {b_count} {w_count}')
'''