# 백준 16929. Two Dots
import sys
from collections import deque
sys.stdin = open("bj16929input.txt")

def bfs(y, x, color):
    visited = [[0] * M for _ in range(N)]
    que = deque()

    visited[y][x] = 1
    que.append((y, x))
    while que:
        i, j = que.popleft()
        for di, dj in dir:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == color:
                if visited[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + 1
                    que.append((ni, nj))
                elif ni == y and nj == x and visited[i][j] >= 4:
                    return True
    return False


# start : 시작 좌표
# i, j : 현재 방문 좌표
# c : count(cycle 판별용)
# color : arr[start[0]][start[1]]의 색깔
def dfs(i, j, c, color, start):
    global flag
    # 이미 결과 나옴 -> 종료
    if flag:
        return
    for di, dj in dir:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M:
            # 같은 색깔에 대해
            if arr[ni][nj] == color:
                # 사이클 발견 -> flag 갱신 후 종료
                if c >= 4 and ni == start[0] and nj == start[1]:
                    flag = True
                    return
                # 같은 색의 새로운 방문 -> 재귀 진행
                if visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    dfs(ni, nj, c+1, color, start)



# 원래 T는 없음
T = int(input())
for tc in range(T):
    # N, M : 게임판의 가로와 세로 길이(2 <= N, M <= 50)
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    flag = False
    # arr[i][j]와 같은 색으로 이루어진 사이클 존재 파악
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        if flag:
            break
        for j in range(M):
            visited = [[0] * M for _ in range(N)]
            visited[i][j] = 1
            color = arr[i][j]
            start = (i, j)
            dfs(i, j, 1, color, start)
            if flag:
                print('Yes')
                break
    if not flag:
        print('No')