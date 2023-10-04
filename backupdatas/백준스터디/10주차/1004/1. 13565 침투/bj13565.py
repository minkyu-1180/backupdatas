# 백준 13565. 침투
import sys
sys.stdin = open("bj13565input.txt")
from collections import deque

def bfs(y, x):
    global result
    que = deque()
    que.append((y, x))

    while que:
        i, j = que.popleft()
        if i == 0:
            result = 'YES'
            return
        for di, dj in dir:
            ni = i + di
            nj = j + dj
            if (0 <= ni < M and 0 <= nj < N) and arr[ni][nj] == '0' and visited[ni][nj] == 0:
                que.append((ni, nj))
                visited[ni][nj] = 1

    return



T = int(input())
for tc in range(T):
    M, N = map(int, input().split())
    # 각각 str형으로 받아짐
    arr = [list(input()) for _ in range(M)]
    visited = [[0] * N for _ in range(M)]
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    starts = []
    for i in range(N):
        if arr[M-1][i] == '0':
            starts.append([M-1, i])

    result = 'NO'
    for y, x in starts:
        if result == 'YES':
            break
        if visited[y][x] == 0:
            bfs(y, x)

    print(result)