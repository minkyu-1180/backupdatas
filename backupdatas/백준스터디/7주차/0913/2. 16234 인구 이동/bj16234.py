# 백준 16234. 인구 이동
import sys
sys.stdin = open("bj16234input.txt")

T = int(input())
for tc in range(T):
    N, L, R = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    while True:
        # 현재 소속 연합이 있는지

        yeonhap_list = []
        visited = [[0] * N for _ in range(N)]
        for y in range(N):
            for x in range(N):
                # 아직 연합국에 속해있지 않았을 경우(연합 가능 불가능 여부 모름)
                if visited[y][x] == 0:
                    now = arr[y][x]
                    yeonhap = [(y, x)]
                    visited[y][x] = 1
                    stack = []

                    i = y
                    j = x
                    while True:
                        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                            ni = i + di
                            nj = j + dj
                            if 0 <= ni < N and 0 <= nj < N:
                                if visited[ni][nj] == 0 and L <= abs(arr[i][j] - arr[ni][nj]) <= R:
                                    stack.append((i, j))
                                    i, j = ni, nj
                                    visited[i][j] = 1
                                    yeonhap.append((i, j))
                                    break
                        else:
                            if stack:
                                i, j = stack.pop()
                            else:
                                break
                    # 본인 제외 연합국이 있을 경우(연합 가능)
                    if len(yeonhap) > 1:
                        yeonhap_list.append(yeonhap)
                    else:
                        break

        # 연합 가능 X
        if len(yeonhap_list) == 0:
            break
        else:
            for yeonhap in yeonhap_list:
                yeonhap_sum = 0
                yeonhap_num = len(yeonhap)
                for i, j in yeonhap:
                    yeonhap_sum += arr[i][j]
                mean_v = yeonhap_sum // yeonhap_num
                for i, j in yeonhap:
                    arr[i][j] = mean_v
            result += 1

    print(result)

















    '''
    c = 0
    while c < 2000:
        not_yeonhap = []
        yeonhap_sum = 0
        for i in range(N):
            for j in range(N):
                dir_check = 0  # 하나라도 뜷려있으면 1로
                for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < N and 0 <= nj < N:
                        if L <= abs(arr[i][j] - arr[ni][nj]) <= R:
                            dir_check = 1
                            break
                if dir_check == 0:
                    not_yeonhap.append((i, j))
                else:
                    yeonhap_sum += arr[i][j]
        # 연합 불가능
        if yeonhap_sum == 0:
            break

        mean_v = yeonhap_sum // (N**2 - len(not_yeonhap))
        for i in range(N):
            for j in range(N):
                if (i, j) not in not_yeonhap:
                    arr[i][j] = mean_v
        c += 1

    print(arr)
    print(c)
    '''