# 백준 1012. 유기농 배추
import sys
sys.stdin = open("1012input.txt")

T = int(input())
for test_case in range(1, T+1):
    # M : 가로(1 ~ 50)
    # N : 세로(1 ~ 50)
    # K : 배추심어진 위치 개수(1 ~ 2500)
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    # (i, j)의 방문 여부
    visited = [[0] * M for _ in range(N)]

    # 배추가 모여있는 지역의 수(= 지렁이 최소 마리 수)
    c = 0

    # 갈림길 간선의 노드를 담을 스택
    stack = []
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for y in range(N):
        for x in range(M):
            # 방문할 고려가 필요한 경우
            if arr[y][x] == 1 and visited[y][x] == 0:
                i = y
                j = x
                while True:
                    # 해당 (i, j) 방문 표시
                    visited[i][j] = 1
                    for k in range(4):
                        ni = i + di[k]
                        nj = j + dj[k]
                        # (i, j) 기준 네 방향 방문 준비
                        if 0 <= ni < N and 0 <= nj < M:
                            # 인접한 곳이 방문 고려해야할 경우
                            if visited[ni][nj] == 0 and arr[ni][nj] == 1:
                                # 현재 방문중인 노드 스택에 추가
                                stack.append([i, j])

                                # 새롭게 방문할 노드 선택
                                i = ni
                                j = nj
                                visited[i][j] = 1
                                break
                    else:
                        if stack:
                            i, j = stack.pop()
                        else:
                            c += 1
                            break


    print(c)
