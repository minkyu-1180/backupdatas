import sys
sys.stdin = open("bj15683input.txt")

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())

    office = [list(map(int, input().split())) for _ in range(N)]
    cctvs = []
    visited = [[0] * M for _ in range(N)]

    # CCTV 저장
    for i in range(N):
        for j in range(M):
            if 1 <= office[i][j] < 6:
                cctvs.append((office[i][j], i, j))

    # cctvs.sort(key = lambda x : x[0])
    print(cctvs)
    # 사각지대 최대값
    noview = N * M + 1


    def CCTV(cctvs, n):
        global visited, noview

        # CCTV 모든 대수를 적용시킨 경우 계산
        if n > len(cctvs):
            sagak = 0
            for i in range(N):
                for j in range(M):
                    if visited[i][j] == 0 and office[i][j] != 6:
                        sagak += 1
            noview = min(noview, sagak)
            return

        cctv = cctvs[n - 1]
        number, i, j = cctv

        # 북 동 남 서
        di = [1, 0, -1, 0]
        dj = [0, 1, 0, -1]

        # 1,2,3,4,5번 CCTV 방향
        cctv_direction = [[[0], [1], [2], [3]],
                          [[0, 2], [1, 3]],
                          [[0, 1], [1, 2], [2, 3], [3, 0]],
                          [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
                          [[0, 1, 2, 3]]]

        # 해당하는 번호의 CCTV 방향 적용
        observing_case = cctv_direction[number - 1]

        # 해당 번호의 경우들 적용
        for observing in observing_case:
            # 해당 경우의 방향들
            for k in observing:
                number, i, j = cctv
                # 방문한 적이 없는 경우 해당 CCTV 방문 표시
                if visited[i][j] == 0:
                    visited[i][j] = n
                while True:
                    ni, nj = i + di[k], j + dj[k]
                    if 0 <= ni < N and 0 <= nj < M:  # office 범위 내에서
                        if office[ni][nj] == 6:  # 벽인 경우 중단
                            break
                        else:  # 아닌 경우 방문
                            if visited[ni][nj] == 0:  # 지나간적 없는 경우만 해당 CCTV 방문 표시
                                visited[ni][nj] = n
                            i = ni
                            j = nj
                    else:
                        break

            # 그다음 CCTV 재귀 실시
            CCTV(cctvs, n + 1)

            # 아닌 경우 다시 원상복구
            number, i, j = cctv
            for k in observing:
                if visited[i][j] == n:  # 해당 CCTV가 처음으로 지나갔던 경우 초기화
                    visited[i][j] = 0
                while True:
                    ni, nj = i + di[k], j + dj[k]
                    if 0 <= ni < N and 0 <= nj < M:
                        if office[ni][nj] == 6:  # 벽인 경우 중단
                            break
                        else:
                            if visited[ni][nj] == n:  # 해당 CCTV가 처음으로 갔던 곳만 초기화
                                visited[ni][nj] = 0
                            i = ni
                            j = nj
                    else:
                        break


    CCTV(cctvs, 1)
    print(noview)