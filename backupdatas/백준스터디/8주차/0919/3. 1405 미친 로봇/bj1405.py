# 백준 1405. 미친 로봇
import sys
sys.stdin = open("bj1405input.txt")

def backtracking(c, i, j, per):
    global result

    if c == N:
        result += per
        return
    for k in range(4):
        di, dj = dir[k]
        ni, nj = i+di, j+dj

        # 이미 방문한 곳이 아니라면
        if not visited[ni][nj]:
            visited[ni][nj] = 1
            backtracking(c+1, ni, nj, per * dir_per[k])
            visited[ni][nj] = 0


T = int(input())
for tc in range(T):
    lst = list(map(int, input().split()))
    N = lst[0]
    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    dir_per = []
    for i in range(1, len(lst)):
        dir_per.append(lst[i]/100)
    # 방문 한 곳
    visited = [[0] * (2*N+1) for _ in range(2*N+1)]
    # 시작점 방문 처리
    visited[N][N] = 1
    #
    result = 0
    backtracking(0, N, N, 1)
    print(result)