# 백준 1303. 주사위
import sys
from collections import deque
sys.stdin = open("bj1303input.txt")


def bfs(color, y, x):
    que = deque()
    visited[y][x] = 1
    que.append((y, x))
    c = 1
    while que:
        i, j = que.popleft()
        for di, dj in dir:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == color and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                que.append((ni, nj))
                c += 1
    result[color] += c**2



M, N = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

result = {
          'W' : 0,
          'B' : 0,
          }
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            bfs(arr[i][j], i, j)
print(result['W'], result['B'])