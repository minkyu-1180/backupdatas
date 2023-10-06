# 백준 1743. 음식물 피하기
import sys
sys.stdin = open("bj1743input.txt")
from collections import deque

def bfs(i, j):
    c = 1
    que = deque()
    que.append((i, j))

    while que:
        y, x = que.popleft()
        for dy, dx in dir:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == 1 and visited[ny][nx] == -1:
                visited[ny][nx] += visited[y][x] + 1
                que.append((ny, nx))
                c += 1
    return c


N, M, K = map(int, input().split())

result = 0
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
visited = [[-1] * M for _ in range(N)]

arr = [[0] * M for _ in range(N)]
trash_idx = []
for _ in range(K):
    r, c = map(int, input().split())
    trash_idx.append((r-1, c-1))
    arr[r-1][c-1] = 1


for k in range(K):
    i, j = trash_idx[k]
    if visited[i][j] == -1:
        visited[i][j] = 0
        c = bfs(i, j)
        if result < c:
            result = c
print(result)