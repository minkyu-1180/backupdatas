# 백준 14940. 쉬운 최단거리
import sys
sys.stdin = open("bj14940input.txt")
from collections import deque

def bfs():
    while que:
        i, j = que.popleft()
        for di, dj in dir:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                result[ni][nj] = result[i][j] + 1
                que.append([ni, nj])



N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
result = [[-1] * M for _ in range(N)]
que = deque()

dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            que.append([i, j])
            visited[i][j] = 1
            result[i][j] = 0 # 2도 0으로 침
        elif arr[i][j] == 0:
            result[i][j] = 0

bfs()

for i in range(N):
    for j in range(M):
        print(result[i][j], end = ' ')
    print()