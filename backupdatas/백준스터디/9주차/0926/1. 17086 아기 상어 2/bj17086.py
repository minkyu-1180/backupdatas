# 백준 17086. 아기 상어 2
import sys
from collections import deque
sys.stdin = open("bj17086input.txt")

def bfs():
    global result

    min_dist = int(1e9)
    while que:
        i, j = que.popleft()
        if arr[i][j] == 1 and min_dist > visited[i][j]:
            min_dist = visited[i][j]
            break

        for di, dj in dir:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == -1:
                visited[ni][nj] = visited[i][j] + 1
                que.append((ni, nj))
    if result < min_dist:
        result = min_dist
    return
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dir = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    result = 0
    for i in range(N):
        for j in range(M):
            visited = [[-1] * M for _ in range(N)]
            visited[i][j] = 0
            que = deque()
            que.append((i, j))
            bfs()
    print(result)
