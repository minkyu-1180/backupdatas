# 백준 2178. 미로 탐색
import sys
from collections import deque
sys.stdin = open("bj2178input.txt")

def bfs():
    visited = [[-1] * M for _ in range(N)]
    visited[0][0] = 1
    que = deque()
    que.append((0, 0))
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    while que:
        i, j = que.popleft()
        if i == N-1 and j == M-1:
            return visited[i][j]
        for di, dj in dir:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1:
                if visited[ni][nj] == -1:
                    visited[ni][nj] = visited[i][j] + 1
                    que.append((ni, nj))




# 원래 T는 없음
T = int(input())
for tc in range(T):
    # N : 세로(2 <= N, M <= 1000)
    # M : 가로
    N, M = map(int, input().split())
    # arr[i][j] == 0 : 이동 불가
    # arr[i][j] == 1 : 이동 가능
    arr = [list(map(int, input())) for _ in range(N)]
    # 목적 : (0, 0) -> (N-1, M-1)로 이동시 최소 칸 수
    result = bfs()
    print(result)