# swea 5250. 최소 비용
import sys
sys.stdin = open("swea5250input.txt")
T = int(input())

def dijkstra(y, x):
    pq = []
    pq.append((y, x, 0))
    dist[y][x] = 0
    while pq:
        i, j, w = pq.pop(0)

        if dist[i][j] < w:
            continue
        dist[i][j] = w

        for di, dj in dir:
            ni = i + di
            nj = j + dj

            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] - arr[i][j] > 0:
                    plus = arr[ni][nj] - arr[i][j] + 1
                else:
                    plus = 1
                if dist[ni][nj] <= w + plus:
                    continue
                dist[ni][nj] = w + plus
                pq.append((ni, nj, w + plus))


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]


    INF = int(1e9)
    dist = [[INF] * N for _ in range(N)]
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    dist = [[INF] * N for _ in range(N)]
    dijkstra(0, 0)
    result = dist[N-1][N-1]
    for i in range(N):
        print(dist[i])
    print(f'#{tc} {result}')


