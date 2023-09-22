# swea 1251. 하나로
import heapq
import sys
sys.stdin = open("swea1251input.txt")

def prim(start):
    pq = []
    MST = [0] * N

    heapq.heappush(pq, (0, start))
    sum_w = 0

    while pq:
        w, now = heapq.heappop(pq)

        if MST[now]:
            continue
        MST[now] = 1

        sum_w += w
        for next in range(N):
            if graph[now][next] == 0 or MST[next]:
                continue
            heapq.heappush(pq, (graph[now][next], next))
    return sum_w

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x_s = list(map(int, input().split()))
    y_s = list(map(int, input().split()))
    E = float(input())

    graph = [[0] * N for _ in range(N)]
    vertices = []
    for i in range(N):
        y = y_s[i]
        x = x_s[i]
        vertices.append([y, x])

    for i in range(N):
        for j in range(N):
            if i != j:
                y1, x1 = vertices[i]
                y2, x2 = vertices[j]
                L = (x1 - x2) ** 2 + (y1 - y2) ** 2
                w = E * L
                graph[i][j] = w
                graph[j][i] = w
    # graph[i][j] : i -> j로 가는데 필요한 환경 부담금
    result = prim(0)
    print(f'#{tc} {round(result)}')

