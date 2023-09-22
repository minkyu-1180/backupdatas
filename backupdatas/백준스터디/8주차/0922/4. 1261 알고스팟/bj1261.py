# 백준 1261. 알고스팟
import heapq
import sys
sys.stdin = open("bj1261input.txt")
input = sys.stdin.readline

def dijkstra(y, x, c):
    pq = []
    heapq.heappush(pq, (c, y, x))

    while pq:
        w, i, j = heapq.heappop(pq)

        if cost[i][j] < w:
            continue

        for di, dj in dir:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if (cost[ni][nj] == -1) or (cost[ni][nj] > w + arr[ni][nj]):
                    cost[ni][nj] = w+arr[ni][nj]
                    heapq.heappush(pq, (w+arr[ni][nj], ni, nj))

T = int(input())
for tc in range(T):
    M, N = map(int, input().split())
    arr = [list(map(int, input().strip())) for _ in range(N)]

    INF = int(1e9)
    cost = [[-1] * M for _ in range(N)]
    cost[0][0] = 0
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    dijkstra(0, 0, 0)
    print(cost[N - 1][M - 1])
