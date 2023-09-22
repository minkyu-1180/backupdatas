# 백준 2665. 미로 만들기
import heapq
import sys
sys.stdin = open("bj2665input.txt")

def dijkstra(y, x, c):
    pq = []
    heapq.heappush(pq, (c, y, x))

    while pq:
        w, i, j = heapq.heappop(pq)

        if cost[i][j] < w:
            continue
        cost[i][j] = w

        for di, dj in dir:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N:
                # k = 1
                # if arr[ni][nj]:
                #     k = 0
                l = int(not arr[ni][nj])

                if cost[ni][nj] <= w + l:
                    continue
                cost[ni][nj] = w + l
                heapq.heappush(pq, (w+l, ni, nj))

N = int(input().strip())
arr = [list(map(int, input().strip())) for _ in range(N)]
# print(arr)
# 해당 idx까지 도달하는데 부신 문의 개수
INF = int(1e9)
cost = [[INF] * N for _ in range(N)]
cost[0][0] = 0
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

dijkstra(0, 0, 0)
print(cost[N-1][N-1])
