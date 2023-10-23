# 백준 10026. 적록색약
import sys
from collections import deque
sys.stdin = open("bj10026input.txt")

# 적록색약인데 시작 color가 R이나 G인 경우
def bfs_for_RG(i, j, visited):
    que = deque()
    que.append((i, j))
    visited[i][j] = 1
    while que:
        i, j = que.popleft()
        for di, dj in dir:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                if arr[ni][nj] == 'R' or arr[ni][nj] == 'G':
                    visited[ni][nj] = 1
                    que.append((ni, nj))
    return

# 일반인이거나 적록색약인데 시작 color가 B인 경우
def bfs(i, j, color, visited):
    que = deque()
    que.append((i, j))
    visited[i][j] = 1
    while que:
        i, j = que.popleft()
        for di, dj in dir:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                if arr[ni][nj] == color:
                    visited[ni][nj] = 1
                    que.append((ni, nj))
    return

# N : 그리드의 크기(1 <= N <= 100)
N = int(input())
# grid(R, G, B)
arr = [list(input()) for _ in range(N)]
visited_for_not_blindness = [[0] * N for _ in range(N)]
visited_for_blindness = [[0] * N for _ in range(N)]

result_for_not_blindness = 0
result_for_blindness = 0
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for i in range(N):
    for j in range(N):
        color = arr[i][j]
        # 적록색약이 없는 경우 -> 일반적인 bfs 진행
        if visited_for_not_blindness[i][j] == 0:
            bfs(i, j, color, visited_for_not_blindness)
            result_for_not_blindness += 1
        # 적록색약이 있는 경우 : color가 B인지, R이나G인지가 중요
        if visited_for_blindness[i][j] == 0:
            if color == 'B':
                bfs(i, j, color, visited_for_blindness)
            else:
                bfs_for_RG(i, j, visited_for_blindness)
            result_for_blindness += 1
print(result_for_not_blindness, result_for_blindness)