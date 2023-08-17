# 백준 4963. 섬의 개수
# 가로, 세로, 대각선 연결된 land : 걸어갈 수 있음(한 개의 섬에 포함)
import sys
sys.stdin = open("4963input.txt")

while True:
    # M : 너비(w) / N : 높이(h)
    # <= 50

    M, N = map(int, input().split())
    if M == 0 and N == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    # 갈 수 있는 경로 : 인접 8곳
    di = [-1, -1, -1, 0, 0, 1, 1, 1]
    dj = [-1, 0, 1, -1, 1, -1, 0, 1]

    visited = [[0] * M for _ in range(N)]
    stack = []
    # 섬의 개수
    c = 0
    for y in range(N):
        for x in range(M):
            if arr[y][x] == 1 and visited[y][x] == 0:
                i = y
                j = x
                while True:
                    visited[i][j] = 1
                    for k in range(8):
                        ni = i + di[k]
                        nj = j + dj[k]
                        if 0 <= ni < N and 0 <= nj < M:
                            if visited[ni][nj] == 0 and arr[ni][nj] == 1:
                                stack.append([i, j])
                                i = ni
                                j = nj
                                visited[i][j] = 1
                                break
                    else:
                        if stack:
                            i, j = stack.pop()
                        else:
                            c += 1
                            # print(f'종료된 시점의 방문노드 : {i, j}')
                            # print(f'c : {c}')
                            break
    print(c)


